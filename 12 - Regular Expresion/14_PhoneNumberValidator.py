"""
Phone Number Validator

You are given a number input, and need to check if it is a valid phone number.
A valid phone number has exactly 8 digits and starts with 1, 8 or 9.
Output "Valid" if the number is valid and "Invalid", if it is not.

Sample Input
81239870

Sample Output
Valid
"""
import re

number = input("Enter a number: ")
pattern = r"[^2-7]{1}[0-9]{7}$"
match = re.match(pattern, number)
if match:
    print("Valid")
else:
    print("Invalid")