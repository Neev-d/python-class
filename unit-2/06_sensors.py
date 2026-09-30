"""Sensor helpers for the mission console."""

THRESHOLD = 70.0

def is_alert(value):
    """True whe a reading exceeds the alert threshold."""
    return value > THRESHOLD

def average(values):
    """Mean of a list of readings."""
    return sum(values)/len(values)
if __name__ == '__main__':
    print("self-test:", is_alert(85), average([10, 20, 30]))