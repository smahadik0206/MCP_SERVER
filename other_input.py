from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import List

mcp = FastMCP('Other Inputs')

class Person(BaseModel):
    first_name : str = Field(..., description='The person first name')
    last_name : str = Field(..., description='The person last name')
    years_of_experince : int = Field(..., description='Number of years of experience')
    previous_addresses : List[str] = Field(default_factory=list, description='List of previous residential addresses')
    
@mcp.tool()
def add_person_to_member_database(person: Person)->str:
    """Logs the personal details of the given person to the database.
    Args:
        person (Person): An instance fo the Person class containing the following personal deails:
        -first_name (str): The person's given name.
        -last_name (str): The person's family name.
        -years_of_experience (int): Number of years of experince.
        -pervious_addresses (List[str]): A list of the person's previous residential addresses
    Returns:
        str; A confirmation message indication that the data has been logged
    """
    with open("C:/MCP/weather/log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"First Name: {person.first_name}\n")
        log_file.write(f"Last Name: {person.last_name}\n")
        log_file.write(f"years of Exprerience: {person.years_of_experince}\n")
        log_file.write(f"Previous Addresses: {person.previous_addresses}\n")
        
        for idx, address in enumerate(person.previous_addresses, 1):
            log_file.write(f" {idx}. {address}\n")
        log_file.write("\n")
        
    return "Data has been logged"


if __name__ == "__main__":
    mcp.run()
    
    
    
# Input
# log the following person to db: Henry Habib, nine years of exp, he has previously lived in 444 Pune road and Wakad 125 st road
    
# ***Notes****
# class WeatherInput(BaseModel):
#     location: str

# class WeatherOutput(BaseModel):
#     temperature: float
#     description: str

# @tool()
# def get_weather(data: WeatherInput) -> WeatherOutput:
#     # (Simulated logic)
#     return WeatherOutput(
#         temperature=34.5,
#         description="hot and sunny"
#     )
