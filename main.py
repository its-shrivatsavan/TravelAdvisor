from textwrap import dedent
import os
from travelcrew import TravelAdvisorCrew

if __name__ == "__main__":
    print("## Welcome to TravelAdvisor 🚢🌊")
    # print("-------------------------------------")
    # location = input(dedent("""
    #             Where are you travelling from? 
    #                         """))
    # cities = input(dedent(
    #     """
    #     What are the city options you are interested in visiting? 
    #     """
    # ))
    # data_range = input(dedent(
    #     """
    #     What is the date range you are interested in visiting?
    #     """
    # ))
    # interests = input(dedent("""
    #             What are some of your interests and hobbies?
    #             """))
    
    crew_instance = TravelAdvisorCrew(
        origin= 'Bangalore',
        cities= 'Kashmir',
        date_range= '24-05-2025',
        interests= 'Visiting scenic places'
    )

    result = crew_instance.travelcrew().kickoff()
    print(result)

    