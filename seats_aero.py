import requests

url = "https://seats.aero/api/availability"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Assuming the response is in JSON format
    # Process the data as needed
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
