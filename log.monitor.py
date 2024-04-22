import time
import signal
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='log_monitor.log')

def signal_handler(sig, frame):
    print("\nMonitoring interrupted. Exiting.")
    sys.exit(0)

# Define log file path
log_file_path = "your_log_file.log"
# Make sure to replace "your_log_file.log" with the path to the log file you want to monitor.

# Define keywords to monitor
keywords_to_monitor = ["ERROR", "HTTP"]

def monitor_log():
    try:
        with open(log_file_path, 'r') as file:
            file.seek(0, 2)  # Go to the end of the file
            while True:
                line = file.readline()
                if line:
                    for keyword in keywords_to_monitor:
                        if keyword in line:
                            logging.info("Keyword found: %s - %s" % (keyword, line.strip()))
                time.sleep(0.1)
    except FileNotFoundError:
        logging.error("Log file not found at path: %s" % log_file_path)
        sys.exit(1)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)

    logging.info("Starting log monitoring for file: %s" % log_file_path)
    try:
        monitor_log()
    except Exception as e:
        logging.error("An error occurred: %s" % str(e))
