import time
import requests
from functools import wraps

def retry_request(max_retries=3, backoff_factor=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.RequestException:
                    retries += 1
                    time.sleep(backoff_factor * (2 ** retries))
            raise Exception('Max retries exceeded')
        return wrapper
    return decorator

@retry_request(max_retries=5, backoff_factor=0.5)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()