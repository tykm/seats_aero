import json

def filter(data, origins=None, destinations=None):
    filtered_array = [item for item in data if
        item.get("Route", {}).get("OriginAirport") in origins
        and item.get("Route", {}).get("DestinationAirport") in destinations]
    return filtered_array