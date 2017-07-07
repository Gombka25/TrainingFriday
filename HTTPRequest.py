import requests
from requests.exceptions import ConnectionError


def check_internet_connection():
    url = 'http://www.google.com'
    try:
        response = requests.get(url=url, validate=False)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False