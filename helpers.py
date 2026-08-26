import time
from functools import wraps


def retry_operation(retries=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == retries:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator


def safe_request(url, timeout=5):
    import urllib.request
    import urllib.error

    @retry_operation(retries=3, delay=0.5)
    def _execute():
        req = urllib.request.Request(url, headers={'User-Agent': 'Autoclicker-Agent'})
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status == 200

    try:
        return _execute()
    except Exception:
        return False
