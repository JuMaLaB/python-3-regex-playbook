import re


def extract_ip_addresses(log_line):
    pattern = r"(?:\d{1,3}\.){3}\d{1,3}"

    ip_addresses = re.findall(pattern, log_line)

    for ip in ip_addresses:
        print(f"IP Address: {ip}")


with open("./files/sample1.log", "r") as f:
    for line in f:
        extract_ip_addresses(line)
