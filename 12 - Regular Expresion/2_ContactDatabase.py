"""
Contacts Database
Create a program that will take the phone number as input, 
and if the number starts with '00', replace them with '+'.
"""
import re

number = input("Enter a phone number: ")
pattern = r"00"
newnumber = re.sub(pattern, "+", number)
print(newnumber)