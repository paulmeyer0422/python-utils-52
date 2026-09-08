import time
import urllib.request
import urllib.error
from typing import Callable, Any

class NetworkError(Exception):
    """Custom exception for network operations."""
    pass

def retry_on_failure(retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except (urllib.error.URLError, ConnectionError) as e:
                    if attempt == retries - 1:
                        raise NetworkError(f"Failed after {retries} attempts: {e}") from e
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_on_failure(retries=3, delay=0.5)
def fetch_remote_config(url: str) -> str:
    """Fetches remote configuration for the autoclicker."""
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.read().decode('utf-8')
