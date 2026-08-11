import re

def is_email_valid(email: str) -> bool:
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))


def is_url_valid(url: str) -> bool:
    regex = r'^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, url))


def is_phone_number_valid(phone: str) -> bool:
    regex = r'^\+?\d{10,15}$'
    return bool(re.match(regex, phone))


def is_username_valid(username: str) -> bool:
    regex = r'^[a-zA-Z0-9_]{3,20}$'
    return bool(re.match(regex, username))


def is_strong_password(password: str) -> bool:
    return (len(password) >= 8
            and any(char.isdigit() for char in password)
            and any(char.islower() for char in password)
            and any(char.isupper() for char in password)
            and any(char in '!@#$%^&*()' for char in password))