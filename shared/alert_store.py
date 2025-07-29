from collections import deque

ALERT_BUFFER = deque(maxlen=100)

def add_alert(msg: str):
    ALERT_BUFFER.appendleft(msg)

def get_alerts():
    return list(ALERT_BUFFER)
