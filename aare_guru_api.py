# https://aareguru.existenz.ch/
# This script interacts with the Aare Guru API
# https://aareguru.existenz.ch/

import requests

# Function to get data from the Aare Guru API
def get_aare_data():
    url = "https://aareguru.existenz.ch/v2018/current?app=your_app_name"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Example usage
data = get_aare_data()
if data:
    print(data)
else:
    print("Failed to retrieve data")

# Save the data to a JSON file
import json

file_path = "aare_data.json"
with open(file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)  # indent=4 for pretty formatting

print(f"JSON file saved at {file_path}")