import asyncio
from app.tool.searxng_search import SearxNGSearch

async def main():
    # Replace with a valid SearxNG base URL for actual testing
    searxng = SearxNGSearch(name="test_searxng", description="Test SearxNG search", base_url="http://searx.lan")
    results = await searxng.execute(query="test query")
    for result in results:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
