import logging
from typing import Optional

class Logger:
    """
    A simple logging utility.
    """

    def __init__(self, name: str, level: Optional[int] = logging.INFO) -> None:
        """
        Initializes the logger with the given name and level.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str) -> None:
        """
        Logs a message with level DEBUG.
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Logs a message with level INFO.
        """
        self.logger.info(message)

    def warning(self, message: str) -> None:
        """
        Logs a message with level WARNING.
        """
        self.logger.warning(message)

    def error(self, message: str) -> None:
        """
        Logs a message with level ERROR.
        """
        self.logger.error(message)

    def critical(self, message: str) -> None:
        """
        Logs a message with level CRITICAL.
        """
        self.logger.critical(message)