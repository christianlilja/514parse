from .base_alert import BaseAlert
from shared.alert_store import add_alert

class ConsoleAlert(BaseAlert):
    def send(self, message: str):
        print(f"[ALERT] {message}")
        add_alert(message)
