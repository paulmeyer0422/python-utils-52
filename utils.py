import time
import functools
import logging

logger = logging.getLogger(__name__)

def retry(exceptions, tries=3, delay=1, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            t, d = tries, delay
            while t > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(f'{func.__name__} failed: {e}, retrying in {d}s...')
                    time.sleep(d)
                    t -= 1
                    d *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator

@retry((ConnectionError, TimeoutError), tries=3, delay=2)
def network_request(url):
    # Simulate network operation
    pass