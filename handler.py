import time
import requests

class NetworkHandler:
    def __init__(self, retries=3, backoff_factor=0.5):
        self.retries = retries
        self.backoff_factor = backoff_factor

    def retry_request(self, url):
        attempt = 0
        while attempt < self.retries:
            try:
                response = requests.get(url)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException:
                attempt += 1
                wait_time = self.backoff_factor * (2 ** attempt)
                time.sleep(wait_time)
        raise Exception('Max retries exceeded')

# Example usage:
# handler = NetworkHandler()
# data = handler.retry_request('https://api.example.com/data')