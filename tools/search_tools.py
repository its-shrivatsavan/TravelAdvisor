import os
import json
import requests
from pydantic import BaseModel
from crewai.tools import BaseTool

class SearchInput(BaseModel):
    query: str

class SearchTools(BaseTool):
    name: str = "search_internet"
    description: str = "Function is to search the internet to return relevant results"
    args_schema: type  = SearchInput

    def _run(self, query: str) -> str:
        top_results_to_return = 2
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        try:
            results = response.json()['organic']
        except KeyError:
            return "Sorry, I couldn't find anything. There may be a problem with the Serper API key."

        output = []
        for result in results[:top_results_to_return]:
            try:
                output.append('\n'.join([
                    f"Title: {result['title']}",
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}",
                    "------------------"
                ]))
            except KeyError:
                continue

        return '\n'.join(output)
