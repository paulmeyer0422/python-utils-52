import time
from functools import wraps


def retry(exceptions, tries=3, delay=1, backoff=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return func(*args, **kwargs)
        return wrapper
    return decorator


class NetworkError(Exception):
    pass


@retry((NetworkError, TimeoutError), tries=3, delay=0.5)
def send_network_ping(url):
    import urllib.request
    try:
        response = urllib.request.urlopen(url, timeout=2)
        return response.status == 200
    except Exception as e:
        raise NetworkError(f"Failed to reach {url}: {e}")
