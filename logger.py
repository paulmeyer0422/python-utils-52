import logging
import sys
from typing import Optional


class AutoClickerLogger:
    """Handles application-wide logging for the autoclicker."""

    def __init__(self, name: str = "autoclicker", level: int = logging.INFO) -> None:
        self.logger: logging.Logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        formatter: logging.Formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, message: str) -> None:
        """Log informational messages."""
        self.logger.info(message)

    def error(self, message: str, exc_info: Optional[bool] = False) -> None:
        """Log error messages with optional exception info."""
        self.logger.error(message, exc_info=exc_info)

    def warning(self, message: str) -> None:
        """Log warning messages."""
        self.logger.warning(message)