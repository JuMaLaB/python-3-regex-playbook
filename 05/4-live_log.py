import re
import time
import random

# Simulate getting live logging data
def get_live_logging_data():
    log_levels = ["INFO", "WARNING", "ERROR"]
    log_level = random.choice(log_levels)
    return f"[{log_level}] This is a sample log message."

# Define a function to filter for errors in live logging data
def filter_errors(log_line):
    pattern = r"\[(ERROR)\]"

    match = re.search(pattern, log_line)
    if match:
        print("Error found:", log_line)

# Simulate live logging system
while True:
    line = get_live_logging_data()
    filter_errors(line)
    time.sleep(1)  # Pause for 1 second before fetching the next log entry
