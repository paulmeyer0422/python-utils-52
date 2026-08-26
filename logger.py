import logging
from typing import Any, Dict, Optional, Union
from datetime import datetime

class AutoClickerLogger:
    """Logger for autoclicker operations with click tracking."""

    def __init__(self, name: str = "autoclicker", log_file: Optional[str] = None, level: str = "INFO") -> None:
        """Initialize logger.
        Args:
            name: Logger name.
            log_file: Optional log file path.
            level: Logging level.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, level.upper(), logging.INFO))
        self.click_count: int = 0
        self._configure_handlers(log_file)

    def _configure_handlers(self, log_file: Optional[str]) -> None:
        """Configure handlers.
        Args:
            log_file: Log file or None.
        """
        if not self.logger.handlers:
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            if log_file:
                fh = logging.FileHandler(log_file)
                fh.setFormatter(formatter)
                self.logger.addHandler(fh)

    def log_click(self, x: int, y: int, button: str = "left", delay: float = 0.1) -> None:
        """Log click event.
        Args:
            x: X position.
            y: Y position.
            button: Button name.
            delay: Click delay.
        """
        self.click_count += 1
        self.logger.info(f"Click #{self.click_count} at ({x}, {y}) button={button} delay={delay}")

    def log_warning(self, message: str) -> None:
        """Log warning.
        Args:
            message: Warning message.
        """
        self.logger.warning(message)

    def log_debug(self, message: str, extra: Optional[Dict[str, Any]] = None) -> None:
        """Log debug info.
        Args:
            message: Debug message.
            extra: Extra data dict.
        """
        if extra:
            self.logger.debug(f"{message} {extra}")
        else:
            self.logger.debug(message)

    def get_stats(self) -> Dict[str, Union[int, float, str]]:
        """Get stats.
        Returns:
            Stats dict.
        """
        return {"click_count": self.click_count, "last_updated": datetime.now().isoformat(), "logger_name": self.logger.name}

    def reset_stats(self) -> None:
        """Reset click count."""
        self.click_count = 0

    def set_level(self, level: str) -> None:
        """Set log level.
        Args:
            level: New level.
        """
        self.logger.setLevel(getattr(logging, level.upper(), logging.INFO))