import logging

class ValidationError(Exception):
    pass

def validate_click_params(interval: float, iterations: int) -> None:
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValidationError(f"Invalid interval: {interval}. Must be >= 0.01.")
    if not isinstance(iterations, int) or iterations < -1:
        raise ValidationError(f"Invalid iterations: {iterations}. Must be >= -1.")

def process_input(interval: float, iterations: int):
    try:
        validate_click_params(interval, iterations)
        return True
    except ValidationError as e:
        logging.error(f"Validation failed: {e}")
        return False

def get_sanitized_input(prompt: str, val_type: type):
    user_input = input(prompt)
    try:
        value = val_type(user_input)
        return value
    except ValueError:
        logging.error(f"Invalid type input: {user_input}")
        return None