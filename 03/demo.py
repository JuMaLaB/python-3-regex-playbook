import re
import os

with open("sample1.txt", "r") as f:
    for line in f:
        match = re.search("sample", line)
        if match:
            print("Found a match in line:", line)
            break

print("----------------")
file_extensions = ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"]

with open("sample2.txt", "r") as f:
    text = f.read()
    pattern = r"\b\w+\.(?:" + "|".join(file_extensions) + r")\b"
    matches = re.findall(pattern, text)

print(matches)

# pattern
# r => raw sting (allow to not escape the escape char)
# \b => word boundary => 1st for beginning of a word
# \w => 1 or more word Char
# \. => here it's for a real .
# (?:abc) => non-capturing group
# "|".join(file_extensions) => will concatenate file extension with | between => | = or
# \b => word boundary => end of a word

print("----------------")
phone_pattern = r"\d{3}-\d{3}-\d{4}"
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
zip_pattern = r"\b\d{5}(?:-\d{4})?\b"
order_pattern = r"\b[A-Z]{2}-\d{4}-\d{4}\b"
hex_pattern = r"#[A-Fa-f0-9]{6}"

with open("sample3.txt", "r") as f:
    text = f.read()
    phone_match = re.search(phone_pattern, text)
    email_match = re.search(email_pattern, text)
    zip_match = re.search(zip_pattern, text)
    order_match = re.search(order_pattern, text)
    hex_match = re.search(hex_pattern, text)

if phone_match:
    print(f"Phone number found: {phone_match.group()}")
if email_match:
    print(f"Email address found: {email_match.group()}")
if zip_match:
    print(f"Zip code found: {zip_match.group()}")
if order_match:
    print(f"Order number found: {order_match.group()}")
if hex_match:
    print(f"Hex color code found: {hex_match.group()}")

print("----------------")
with open("sample4.txt", "r") as f:
    text = f.read()

pattern = r"\b[A-Z]{2}\d{2}-[A-Z]{2}\d{2}\b|\b\d{3}-\d{3}\b"
matches = re.findall(pattern, text)

print("All product codes:", matches)


print("----------------")
file_pairs = [
    ("file1.txt", "codes1.txt"),
    ("file2.txt", "codes2.txt"),
    ("file3.txt", "codes3.txt"),
]


def extract_product_codes(file_path, output_file):
    with open(file_path, "r") as f:
        text = f.read()
        pattern = r"\b[A-Z]{2}\d{2}-[A-Z]{2}\d{2}\b|\b\d{3}-\d{3}\b"
        matches = re.findall(pattern, text)

        with open(output_file, "w") as output_f:
            for match in matches:
                output_f.write(f"{match}\n")


for input_file, output_file in file_pairs:
    input_path = os.path.join("input", input_file)
    output_path = os.path.join("output", output_file)
    extract_product_codes(input_path, output_path)
