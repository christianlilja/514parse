from .base_detector import BaseDetector
from alerts.console_alert import ConsoleAlert

class SudoAbuseDetector(BaseDetector):
    def __init__(self):
        self.alert = ConsoleAlert()

    def process_line(self, line: str):
        if "sudo:" in line and "authentication failure" in line:
            self.alert.send(f"Possible sudo abuse detected: {line.strip()}")
