"""
Starts With Ends With
Write a program that takes a word as input, 
and outputs 'Match' if the word has 4 letters, 
starts with 'm' and ends with 'e'.
"""
from ast import pattern
import re
pattern = r"^m..e$"
word = input("Enter a word: ")
match = re.match(pattern, word)
if match:
    print("Match")
else:
    print("No match")