import re

""" ---------------- """

print("----------------")
text = "This is a sample text."
pattern = "sample"
match = re.search(pattern, text)

if match:
    print(f"Found search with pattern: ", pattern, " on: ", text, "and match: ", match)
else:
    print("Not Found !")

""" ---------------- """

print("----------------")
text = "This is a sample text."
pattern = "This"
match = re.match(pattern, text)

if match:
    print(f"Found match with pattern: ", pattern, " on: ", text, "and match: ", match)
else:
    print("Not Found !")

""" ---------------- """

print("----------------")
date_string = "2024-12-12"
pattern = r"\d{4}-\d{2}-\d{2}"
match = re.fullmatch(pattern, date_string)

if match:
    print(
        f"Found fullmatch with pattern: ",
        pattern,
        " on: ",
        date_string,
        "and match: ",
        match,
    )
else:
    print("Not Found !")

""" ---------------- """

print("----------------")
text = "The price of the life is $0 whereas for living you need at least a salary of $2,500.00"
pattern = r"\d+"

matches = re.findall(pattern, text)

if match:
    print(
        f"Found findall with pattern: ",
        pattern,
        " on: ",
        text,
        "and match: ",
        matches,
    )
else:
    print("Not Found !")

""" ---------------- """

print("----------------")
text = "These shitty courses drive me crazy"
pattern_1 = r"\b\w{6}\b"
pattern_2 = r"\bc[a-z]{4}\b"

new_text = re.sub(pattern_1, "nice", text)
new_text = re.sub(pattern_2, "happy", text)

if match:
    print(f"Replace: ", text, " by: ", new_text)
else:
    print("Not Found !")

""" ---------------- """

print("----------------")
text = "These shitty courses drive me crazy"
pattern = r"\s+"

words = re.split(pattern, text)
print(words)

""" ---------------- """

print("----------------")
pattern = r"\b"
text = r"A text with \boundary escape char"

escaped_pattern = re.escape(pattern)
match = re.search(escaped_pattern, text)

if match:
    print(f"Escaped pattern: ", escaped_pattern, " Found !")

""" ---------------- """

print("----------------")
pattern = r"."
text = r"A text with a real dot at the end."

escaped_pattern = re.escape(pattern)
match = re.search(escaped_pattern, text)

if match:
    print(f"Escaped pattern: ", escaped_pattern, " Found !")

""" ---------------- """

print("----------------")
pattern = r"\d+"
text = "The price of the life is $0 whereas for living you need at least a salary of $2,500.00"

regex = re.compile(pattern)
matches = regex.findall(text)

print(f"Regex: ", regex, "matches: ", matches)

""" ---------------- """

print("----------------")
pattern = r"(\d{3})-(\d{3}-\d{4})"  # amtch phone number in format XXX-XXX-XXXX
text = "My phone number is 555-666-1234"

match = re.search(pattern, text)

if match:
    print(f"Matched phone number: {match.group()}")
    print(f"Area code: {match.group(1)}")
    print(f"phone number: {match.group(2)}")
    print(f"Start: {match.start()}")
    print(f"End: {match.end()}")
    print(f"Span: {match.span()}")
