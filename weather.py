import os
import requests
from mcp import tool
from mcp.server.fastmcp import FastMCP

SERPAPI_KEY = '32a0cc3531ab9042d7dc9d82fc57587298d36af624f8e07a8d4d648d63266601'  
mcp = FastMCP('Weather')

@mcp.tool()
def searp_api_get_info(location: str) -> str:
    """
    Gets the weather given a location using SerpAPI
    Args:
        location: location, can be city, state, country etc.
    Returns:
        A short weather description.
    """
    if not SERPAPI_KEY:
        return "SerpAPI key is missing"

    params = {
        "q": f"weather in {location}",
        "api_key": SERPAPI_KEY,
        "engine": "google"
    }

    try:
        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        # # Extract weather data from the response
        weather_box = data.get("weather_result")
        # if not weather_box:
        #     return f"No weather info found for {location}"

        # temp = weather_box.get("temperature")
        # desc = weather_box.get("description")
        return f"{weather_box}"
    
    except Exception as e:
        return f"Error retrieving weather: {str(e)}"
