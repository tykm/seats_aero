import json

def filterDestination(data, dest):
    filtered_array = [item for item in data if item.get("Route", {}).get("DestinationAirport") in dest]
    return filtered_array