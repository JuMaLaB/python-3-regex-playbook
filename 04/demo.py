import re

input_name = input("Enter your name:\n")


def check_name(name):
    pattern = r"^[a-zA-Z]+[\w]*$"
    match = re.fullmatch(pattern, name)
    return match is not None


if check_name(input_name):
    print("Ok !")
else:
    print("Not Ok !")

print("----------------")
input_number = input("Enter your number:\n")


def check_number(number):
    # pattern = r"^\d+$"
    pattern = r"^-?\d+(\.\d)?$"
    match = re.search(pattern, number)
    return match is not None


if check_number(input_number):
    print("Ok !")
else:
    print("Not Ok !")
