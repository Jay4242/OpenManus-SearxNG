# SearxNG Search Tool

## Description

This tool allows an agent to search a SearxNG instance and extract URLs and titles from the search results. It is designed to be used within an automated agent framework.

## Usage

### Initialization

To use the `SearxNGSearch` tool, you need to initialize it with the base URL of your SearxNG instance.

```python
from app.tool.searxng_search import SearxNGSearch

searxng = SearxNGSearch(name="searxng_search", description="A tool for searching a SearxNG instance.", base_url="YOUR_SEARXNG_BASE_URL")
```

Replace `YOUR_SEARXNG_BASE_URL` with the actual base URL of your SearxNG instance.

### Execution

The tool's `execute` method takes a search query as input and returns a list of strings, where each string contains the title, URL, and description of a search result.

```python
results = await searxng.execute(query="your search query")
for result in results:
    print(result)
```

### Input

The `execute` method requires a `query` parameter, which is a string representing the search query.

### Output

The `execute` method returns a list of strings. Each string in the list represents a search result and contains the title, URL, and description, separated by " | ". If an error occurs during the search, the list will contain a single string with an error message.

## Dependencies

- `requests`: For making HTTP requests to the SearxNG instance.
- `beautifulsoup4`: For parsing the HTML content of the search results.
- `pydantic`: For data validation and settings management.

## Configuration

The following parameters can be configured:

- `base_url`: The base URL of the SearxNG instance. This is a required parameter during initialization.
- `user_agent`: The user agent string used for making HTTP requests. The default value is "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36".

## Error Handling

The tool handles potential errors during the search process, such as network issues or invalid responses from the SearxNG instance. If an error occurs, the `execute` method returns a list containing an error message.

## Details

### Class: SearxNGSearch

Bases: `app.tool.base.BaseTool`

A tool for searching a SearxNG instance and extracting URLs and titles.

#### Attributes:

- `name` (str): The name of the tool ("searxng_search").
- `description` (str): A description of the tool.
- `base_url` (str): The base URL of the SearxNG instance.  This must be provided when initializing the tool.
- `user_agent` (str): The user agent string used for making HTTP requests.
- `parameters` (dict): A dictionary defining the input parameters for the tool.

#### Input Model: SearxNGSearch.Input

- `query` (str): The search query string.

#### Methods:

- `__init__(self, **kwargs)`: Initializes the SearxNGSearch tool.  Requires the `base_url` to be set.
- `execute(self, query: str) -> List[str]`: Executes the search query and returns a list of results.

### Usage Notes:

- Ensure the SearxNG instance is accessible from the environment where the tool is being used.
- The tool uses `requests` library, so ensure it is installed (`pip install requests`).
- The tool uses `beautifulsoup4` library for HTML parsing, so ensure it is installed (`pip install beautifulsoup4`).
- The tool disables SSL verification (`verify=False`) in the `requests.post` call. This is potentially insecure and should be addressed in a production environment by properly configuring SSL verification.
- The `safesearch` parameter is hardcoded to `0` (disabled).
- The `theme` parameter is hardcoded to `simple`.
