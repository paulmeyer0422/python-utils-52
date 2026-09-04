import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=3, delay=1, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f"{e}, retrying in {mdelay}s...")
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

class NetworkProcessor:
    @retry((ConnectionError, TimeoutError), tries=3, delay=2)
    def fetch_data(self, url):
        # Simulated network operation
        pass

    @retry((IOError,), tries=2, delay=1)
    def send_click_event(self, event_data):
        # Simulated server communication
        pass