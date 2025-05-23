from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_core.rate_limiters import InMemoryRateLimiter

from tools.search_tools import SearchTools
from tools.calculator_tool import CalculateTool
import yaml
import litellm

load_dotenv()
# litellm._turn_on_debug()
rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.4,        # 12 requests per minute
    check_every_n_seconds=0.2,      # how frequently to check token bucket
    max_bucket_size=2               # allows small bursts
)

@CrewBase
class TravelAdvisorCrew:
    """Travel Advisor Crew"""
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

        with open("config/agents.yaml", "r") as f:
            self.agent_config = yaml.safe_load(f)
        with open("config/tasks.yaml", "r") as f:
            self.task_config = yaml.safe_load(f)


        self.llm = ChatGroq(model="groq/llama-3.3-70b-versatile")
        self.search_tool = SearchTools()
        self.calculate_tool = CalculateTool()
    
    @agent
    def local_tour_guide(self) -> Agent:
        return Agent(
            config=self.agent_config["local_tour_guide"],
            tools=[self.search_tool,],
            llm=self.llm,
            verbose=True
        )
    
    @agent
    def travel_concierge(self) -> Agent:
        return Agent(
            config=self.agent_config["travel_concierge"],
            tools=[self.search_tool, self.calculate_tool,],
            llm=self.llm,
            verbose=True
        )
    
    def plan_itinerary(self, agent, city, travel_dates, interests) -> Task:
        description_template = self.task_config["plan_itinerary"]["description"]
        return Task(
            description=description_template.format(
                city=city,
                travel_dates=travel_dates,
                interests=interests
            ), 
            agent=agent,
            expected_output = self.task_config["plan_itinerary"]["expected_output"]
        )

    def gather_city_info(self, agent, city, travel_dates, interests) -> Task:
        description_template = self.task_config["gather_city_info"]["description"]
        return Task(
            description=description_template.format(
                city=city,
                travel_dates=travel_dates,
                interests=interests
            ), 
            agent=agent,
            expected_output = self.task_config["gather_city_info"]["expected_output"]
        )

    @crew
    def travelcrew(self) -> Crew:
        """ Creates the Travel Advisor Crew"""

        return Crew(
            agents = [self.local_tour_guide(), self.travel_concierge()],
            tasks = [
                self.gather_city_info(
                    agent=self.local_tour_guide(),
                    city=self.cities,
                    travel_dates=self.date_range,
                    interests=self.interests
                ),
                self.plan_itinerary(
                    agent=self.travel_concierge(),
                    city=self.cities,
                    travel_dates=self.date_range,
                    interests=self.interests
                )
            ],
            process=Process.sequential,
            verbose=True
        )

    