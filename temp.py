import os
from mcp.server.fastmcp import FastMCP
from rapidfuzz import fuzz

mcp = FastMCP("MRF Link Extractor")

DATA_FILE = "cms-hpt.txt"

def _parse_data_file(filepath: str) -> list[dict]:
    """
    Parses the multi-record data file into a list of dictionaries.
    Each dictionary represents one location's data.
    """
    records = []
    current_record = {}

    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(': ', 1)
                    if len(parts) == 2:
                        key, value = parts[0].strip(), parts[1].strip()
                        current_record[key] = value
                else:
                    if current_record:
                        records.append(current_record)
                        current_record = {}

            # Add the last record if file doesn’t end with newline
            if current_record:
                records.append(current_record)

    return records

# Load data at startup
all_location_data = _parse_data_file(DATA_FILE)


@mcp.resource("mercy://location//{location_name}")
def get_record_by_hospital_location_details(location_name: str) -> dict:
    """
    Retrieves all details for a given location name from the data file.
    """
    
    THRESHOLD = 85
    for record in all_location_data:
        loc = record.get("location-name", "")
        if fuzz.ratio(loc.lower(), location_name.lower()) >= THRESHOLD:
            return record
    return {"error": f"Location '{location_name}' not any record found."}

@mcp.resource("mercy://mrf_url//{location_name}")
def get_mrf_url_by_location_name(location_name: str) -> str:
    """
    Retrieves the MRF URL for a given location name.
    """
    for record in all_location_data:
        if record.get("location-name", "").lower() == location_name.lower():
            return record.get("mrf-url", "MRF URL not available.")
    return f"Location '{location_name}' not found or MRF URL not available."


@mcp.resource("mercy://contact_email//{location_name}")
def get_contact_email_by_location_name(location_name: str) -> str:
    """
    Retrieves the contact email for a given location name.
    """
    for record in all_location_data:
        if record.get("location-name", "").lower() == location_name.lower():
            return record.get("contact-email", "Contact email not available.")
    return f"Location '{location_name}' not found or contact email not available."


@mcp.resource("mercy://all_locations")
def get_all_mercy_location_names() -> list:
    """
    Returns a sorted list of all unique location names.
    """
    return sorted({
        record.get("location-name") for record in all_location_data if record.get("location-name")
    })


if __name__ == "__main__":
    mcp.run()
