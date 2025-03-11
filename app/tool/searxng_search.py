from typing import List
from pydantic import BaseModel, Field
from app.tool.base import BaseTool
import requests
from bs4 import BeautifulSoup

class SearxNGSearch(BaseTool):
    name: str = "searxng_search"
    description: str = "A tool for searching a SearxNG instance and extracting URLs and titles."
    base_url: str = Field(..., description="The base URL of the SearxNG instance.")
    user_agent: str = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    parameters: dict = {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "(required) The search query.",
            },
        },
        "required": ["query"],
    }

    class Input(BaseModel):
        query: str = Field(..., description="The search query.")

    async def execute(self, query: str) -> List[str]:
        """Executes a search query against a SearxNG instance using POST and extracts URLs and titles."""
        search_url = f"{self.base_url}/search"
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Pragma': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': self.user_agent
        }
        data = f"q={query}&categories=general&language=auto&time_range=&safesearch=0&theme=simple"
        try:
            response = requests.post(search_url, headers=headers, data=data, verify=False)
            response.raise_for_status()
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            results = []
            for article in soup.find_all('article', class_='result'):
                url_header = article.find('a', class_='url_header')
                if url_header:
                    url = url_header['href']
                    title = article.find('h3').text.strip() if article.find('h3') else "No Title"
                    description = article.find('p', class_='content').text.strip() if article.find('p', class_='content') else "No Description"
                    results.append(f"{title} | {url} | {description}")
            return results
        except requests.exceptions.RequestException as e:
            return [f"Error during search: {e}"]
