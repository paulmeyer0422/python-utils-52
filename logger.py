import logging
import sys
from pathlib import Path
from threading import Lock

_lock = Lock()


def get_safe_logger(
    name: str = "autoclicker", log_file: str = "autoclicker.log"
) -> logging.Logger:
    with _lock:
        logger = logging.getLogger(name)
        if logger.handlers:
            return logger

        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - [%(levelname)s] - %(message)s"
        )

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        if not log_file:
            return logger

        try:
            log_path = Path(log_file).resolve()
            log_path.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(
                log_path, mode="a", encoding="utf-8"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (OSError, PermissionError) as err:
            logger.warning(
                "file logging initialization failed, falling back: %s", err
            )

        return logger