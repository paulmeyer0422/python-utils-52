class AutoClickerError(Exception):
    pass

class ConfigurationError(AutoClickerError):
    def __init__(self, message):
        super().__init__(message)

class ClickError(AutoClickerError):
    def __init__(self, message):
        super().__init__(message)

class FrequencyError(AutoClickerError):
    def __init__(self, message):
        super().__init__(message)

class InvalidCoordinatesError(ClickError):
    def __init__(self, x, y):
        message = f"Invalid click coordinates: ({x}, {y})"
        super().__init__(message)

class RateLimitExceededError(FrequencyError):
    def __init__(self, allowed_rate):
        message = f"Rate limit exceeded. Allowed rate: {allowed_rate} clicks per second"
        super().__init__(message)

class MissingConfigurationError(ConfigurationError):
    def __init__(self, config_item):
        message = f"Missing configuration item: {config_item}"
        super().__init__(message)