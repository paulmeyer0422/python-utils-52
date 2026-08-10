import time
import random

RETRY_LIMIT = 5
RETRY_DELAY = 2

class RetryException(Exception):
    pass

def retry_network_operation(func):
    def wrapper(*args, **kwargs):
        for attempt in range(RETRY_LIMIT):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt < RETRY_LIMIT - 1:
                    time.sleep(RETRY_DELAY)
                    continue
                else:
                    raise RetryException(f'Operation failed after {RETRY_LIMIT} attempts') from e
    return wrapper

@retry_network_operation
def mock_network_call():
    if random.random() < 0.7:
        raise Exception('Network failure')
    return 'Success'
