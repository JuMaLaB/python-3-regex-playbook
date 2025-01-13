import re


def split_log_entry(log_line):
    pattern = r"\s+"

    parts = re.split(pattern, log_line)

    print("Date:", parts[0], " / Hours:", parts[1])
    print("Type:", parts[2])
    print("Message:", " ".join(parts[3:]))


with open("./files/sample4.log", "r") as f:
    for line in f:
        split_log_entry(line)
