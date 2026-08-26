import time
def validate_positive_number(value, min_val=1, max_val=10000):
    try:
        num = int(value)
        if min_val <= num <= max_val:
            return num
        return None
    except ValueError:
        return None

def validate_interval(value):
    try:
        num = float(value)
        if 0.1 <= num <= 10:
            return num
        return None
    except ValueError:
        return None

def main():
    print("Autoclicker")
    while True:
        int_str = input("Interval: ")
        interval = validate_interval(int_str)
        if interval is None:
            print("Invalid")
            continue
        cl_str = input("Clicks: ")
        clicks = validate_positive_number(cl_str)
        if clicks is None:
            print("Invalid")
            continue
        break
    for _ in range(clicks):
        print("Performing click")
        time.sleep(interval)
    print("Completed")
if __name__ == "__main__":
    main()