import time
import random
import logging

def validate_click_interval(interval):
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError('Click interval must be a positive number.')


def autoclicker(click_interval, duration):
    validate_click_interval(click_interval)
    if not isinstance(duration, (int, float)) or duration <= 0:
        raise ValueError('Duration must be a positive number.')
    end_time = time.time() + duration
    while time.time() < end_time:
        # Simulate click action
        print('Clicked!')
        time.sleep(click_interval)


if __name__ == '__main__':
    try:
        autoclicker(0.5, 5)
    except ValueError as e:
        logging.error(f'Input error: {e}')