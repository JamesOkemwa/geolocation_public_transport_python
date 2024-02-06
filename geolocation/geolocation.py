import requests

def get_location_from_ip():
    """
    Get the user's location based on their IP address
    """
    URL = "https://ipinfo.io"
    try:
        response = requests.get(URL)
        data = response.json()
        location = data.get('loc').split(",")

        if len(location) == 2:
            return {"lat": float(location[0]), "long": float(location[1])}
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None