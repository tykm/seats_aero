import requests
import json

url = "https://seats.aero/api/availability"
params = {"source": "lifemiles"}
response = requests.get(url, params)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4)  # Indent for better readability
    with open("output.json", "w") as outfile:
        outfile.write(formatted_data)
    print("Data saved to 'output.json'")
else:
    print(f"Request failed with status code: {response.status_code}")
