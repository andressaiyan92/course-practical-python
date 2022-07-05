"""
Cash Out
Fix the program for the ATM machine so that it outputs 'Please enter a number', 
in case the input is not a number.
"""
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a number")