import logging
import sys

def setup_logger(name="autoclicker", log_file="autoclicker.log", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if logger.handlers:
        return logger
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)
    return logger

class ClickLogger:
    def __init__(self, log_file="autoclicker.log"):
        self.logger = setup_logger(log_file=log_file)

    def log_click(self, position, button="left"):
        x, y = position
        self.logger.info(f"Click at ({x}, {y}) using {button} button")

    def log_action(self, action, details=None):
        msg = action
        if details:
            msg += f" - {details}"
        self.logger.info(msg)

    def log_error(self, error_msg):
        self.logger.error(error_msg)

    def log_warning(self, warning_msg):
        self.logger.warning(warning_msg)

    def shutdown(self):
        logging.shutdown()