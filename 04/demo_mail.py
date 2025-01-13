import re

email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
input_email_file_path = input("Enter file path:\n")


def check_email(file_path):
    with open(file_path, "r") as f:
        for line in f:
            if re.search(email_pattern, line):
                print(line)
                with open("./files/valid.txt", "a", encoding="utf-8") as valid_f:
                    valid_f.write(line)
            else:
                print(f"Not Ok ! =>", line)
                with open("./files/invalid.txt", "a", encoding="utf-8") as invalid_f:
                    invalid_f.write(line)


check_email(input_email_file_path)

""" 
with open('email_list.txt', 'r') as input_file:
    email_addresses = input_file.readlines()

invalid_emails = [email.strip() for email in email_addresses if not email_pattern.match(email.strip())]

with open('invalid_emails.txt', 'w') as output_file:
    for invalid_email in invalid_emails:
        output_file.write(f"{invalid_email}\n")
"""
