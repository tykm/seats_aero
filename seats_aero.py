import requests
import json
import helpers

url = "https://seats.aero/api/availability"
all_data = []

# Customize parameters
sources = ["lifemiles", "delta", "virginatlantic"]
destinations = {"EWR", "JFK", "LGA"}

for source in sources:
    params = {"source": source}
    response = requests.get(url, params)
    if response.status_code == 200:
        print(f"AVAILABILITY RECEIVED: {source}")
        data = response.json()
        # Filter data according to custom parameters
        data = helpers.filterDestination(data, destinations)
        all_data.append(data)
    else:
        print(f"Request failed with status code: {response.status_code}")

output_file = "output.json"
with open(output_file, "w") as outfile:
    json.dump(all_data, outfile, indent=4)

print(f"All data saved to '{output_file}'")