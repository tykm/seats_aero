import requests
import json

url = "https://seats.aero/api/availability"
sources = ["lifemiles", "delta", "virginatlantic"]
all_data = []

for source in sources:
    params = {"source": source}
    response = requests.get(url, params)
    if response.status_code == 200:
        data = response.json()
        formatted_data = json.dumps(data, indent=4)  # Indent for better readability
        all_data.append(data)
        print(f"Data received from {source}")
    else:
        print(f"Request failed with status code: {response.status_code}")

output_file = "output.json"
with open(output_file, "w") as outfile:
    json.dump(all_data, outfile, indent=4)

print(f"All data saved to '{output_file}'")