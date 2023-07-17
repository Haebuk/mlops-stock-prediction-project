import os


def load_polygon_api_key():
    """read polygon.io api key
    first check if polygon.api file in local directory exists
    if not, check if environment variable exists
    also if not, raise error
    """
    api_file_path = "polygon.api"
    if os.path.exists(api_file_path):
        with open(api_file_path, "r") as f:
            api_key = f.read()
    elif "POLYGON_API_KEY" in os.environ:
        api_key = os.environ["POLYGON_API_KEY"]
    else:
        raise ValueError("No polygon.io API key found")
    return api_key
