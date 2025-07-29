import config
import time
from detectors.ssh_brute_detector import SSHBruteDetector
from detectors.sudo_abuse_detector import SudoAbuseDetector

def main():
    detectors = [SSHBruteDetector(), SudoAbuseDetector()]

    with open(config.LOG_PATH, "r") as f:
        f.seek(0, 2)  # Move to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.2)
                continue
            for detector in detectors:
                detector.process_line(line.strip())

if __name__ == "__main__":
    main()
