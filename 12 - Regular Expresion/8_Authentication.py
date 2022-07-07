"""
Authentication!
Create a program that takes password as input and returns 'Password created' if all requirements are met.
"""
from ast import pattern
import re

pattern = r"^[a-zA-Z0-9]{8,}$"
password = input("Enter a password: ")
match = re.match(pattern, password)
if match:
    print("Password created")
else:
    print("Wrong format")