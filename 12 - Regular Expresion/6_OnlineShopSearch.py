"""
Online Shop Search
Write a program for a search tool that will take the ID as input and output 
'Searching' if the format is correct, and 'Wrong format', if it's not.
"""
from ast import pattern
import re

# Formar for ID: SHP-12345
pattern = r"^SHP-[0-9][0-9][0-9][0-9][0-9]"
ID = input("Enter an ID: ")
match = re.match(pattern, ID)
if match:
    print("Searching")
else:
    print("Wrong format")