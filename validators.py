import re

def is_valid_email(email: str) -> bool:
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def is_valid_url(url: str) -> bool:
    regex = r'^(http|https)://[\w.-]+(?:\.[\w.-]+)+(\/[\w.-]*)?$'
    return re.match(regex, url) is not None

def is_positive_integer(value: str) -> bool:
    return value.isdigit() and int(value) > 0

def is_non_empty_string(value: str) -> bool:
    return bool(value)

VALIDATORS = {
    'email': is_valid_email,
    'url': is_valid_url,
    'positive_integer': is_positive_integer,
    'non_empty_string': is_non_empty_string,
}