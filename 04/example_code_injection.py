import re

def sanitize_input(input_string):
  sanitized_string = re.sub(r"[;'\"]", "", input_string)
  return sanitized_string

def validate_string_no_code_injection(input_string):
  pattern = r"^[^;'\"]*$"
  match = re.search(pattern, input_string)
  return match is not None

user_input = input("Enter a string to check for code injection: ")
# sanitized_input = sanitize_input(user_input)

if validate_string_no_code_injection(user_input):
  print("Valid input!")
else:
  print("Invalid input. Detected potentially harmful characters.")
