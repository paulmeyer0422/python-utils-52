import time
import logging
from typing import Callable, Any, Tuple, Type

logger = logging.getLogger(__name__)

def retry_network_call(
    tries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Tuple[Type[Exception], ...] = (Exception,)
) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            curr_delay = delay
            for attempt in range(1, tries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == tries:
                        logger.error(f"Failed after {tries} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempt} failed: {e}. Retrying in {curr_delay}s...")
                    time.sleep(curr_delay)
                    curr_delay *= backoff
        return wrapper
    return decorator