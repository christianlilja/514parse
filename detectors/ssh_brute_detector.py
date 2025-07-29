from .base_detector import BaseDetector
from collections import defaultdict
import re
from alerts.console_alert import ConsoleAlert
import config

class SSHBruteDetector(BaseDetector):
    def __init__(self):
        self.failed_attempts = defaultdict(int)
        self.alert = ConsoleAlert()

    def process_line(self, line: str):
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                self.failed_attempts[ip] += 1

                if self.failed_attempts[ip] == config.SSH_FAIL_THRESHOLD:
                    self.alert.send(f"SSH brute-force detected from IP {ip}")
