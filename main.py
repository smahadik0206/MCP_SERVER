from mcp.server.fastmcp import FastMCP
import requests

# SERPAPI_KEY = '32a0cc3531ab9042d7dc9d82fc57587298d36af624f8e07a8d4d648d63266601'  

mcp = FastMCP('WeatherApp')
API_KEY = ''

@mcp.tool()
def get_weather(location:str) -> str:
    """
    Gets the weather given a location
    Args:
        location: location, can be city, state, country etc.
    """

    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return f"Error: {data.get('message', 'Failed to fetch weather')}"

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return f"The weather in {location} is {description} with a temperature of {temp}°C"

    except Exception as e:
        return f"Error retrieving weather: {str(e)}"

if __name__ == "__main__":
    mcp.run()
    