import re


def identify_log_entry_type(log_line):
    pattern = r"(INFO|WARNING|ERROR)"

    match = re.search(pattern, log_line)

    if match:
        log_type = match.group(1)
        print(f"Log Entry Type: {log_type}")


with open("./files/sample1.log", "r") as f:
    for line in f:
        identify_log_entry_type(line)
