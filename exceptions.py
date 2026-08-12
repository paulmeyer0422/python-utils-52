class AutoClickerError(Exception):
    pass

class ConfigurationError(AutoClickerError):
    def __init__(self, message):
        super().__init__(f'Configuration Error: {message}')

class ClickLimitExceeded(AutoClickerError):
    def __init__(self, limit):
        super().__init__(f'Click limit of {limit} exceeded')

class InvalidClickInterval(AutoClickerError):
    def __init__(self, interval):
        super().__init__(f'Invalid click interval: {interval}')

class NotRunningError(AutoClickerError):
    pass

class HandlerError(AutoClickerError):
    def __init__(self, message):
        super().__init__(f'Handler Error: {message}')
