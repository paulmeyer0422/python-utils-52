from typing import Any, Dict, List, Optional

class AutoClickerDataError(Exception):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.details = details or {}

class InvalidDataError(AutoClickerDataError):
    pass

class InvalidClickDataError(InvalidDataError):
    pass

class MissingRequiredFieldError(InvalidDataError):
    def __init__(self, field: str) -> None:
        message = f"Missing required field '{field}' in click data"
        super().__init__(message, {"missing_field": field})

class InvalidCoordinateError(InvalidDataError):
    def __init__(self, coord: str, value: Any) -> None:
        message = f"Invalid {coord} coordinate: {value}"
        super().__init__(message, {"coord": coord, "value": value})

class InvalidIntervalError(InvalidDataError):
    def __init__(self, interval: float) -> None:
        message = f"Invalid interval value: {interval}. Must be positive number"
        super().__init__(message, {"interval": interval})

class DataLoadError(AutoClickerDataError):
    def __init__(self, filepath: str, original_error: Optional[Exception] = None) -> None:
        message = f"Failed to load data from {filepath}"
        details = {"filepath": filepath}
        if original_error:
            details["original_error"] = str(original_error)
        super().__init__(message, details)

class DataSaveError(AutoClickerDataError):
    def __init__(self, filepath: str, original_error: Optional[Exception] = None) -> None:
        message = f"Failed to save data to {filepath}"
        details = {"filepath": filepath}
        if original_error:
            details["original_error"] = str(original_error)
        super().__init__(message, details)

class ClickSequenceValidationError(AutoClickerDataError):
    def __init__(self, sequence: List[Dict[str, Any]], reason: str) -> None:
        message = f"Invalid click sequence: {reason}"
        super().__init__(message, {"sequence_length": len(sequence), "reason": reason})

class RepeatCountError(AutoClickerDataError):
    def __init__(self, count: int) -> None:
        message = f"Invalid repeat count: {count}. Must be positive integer"
        super().__init__(message, {"repeat_count": count})

class ButtonTypeError(AutoClickerDataError):
    def __init__(self, button: str) -> None:
        message = f"Invalid button type: {button}. Use 'left', 'right' or 'middle'"
        super().__init__(message, {"button": button})

class HotkeyError(AutoClickerDataError):
    pass