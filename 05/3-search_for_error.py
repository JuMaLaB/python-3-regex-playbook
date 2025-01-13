import re


def search_for_error_code(log_line, error_code):
    pattern = r"ERROR (\d+)"

    match = re.search(pattern, log_line)
    if match and match.group(1) == error_code:
        print(f"{error_code} error found:", log_line)


with open("./files/sample3.log", "r") as f:
    for line in f:
        search_for_error_code(line, "404")
