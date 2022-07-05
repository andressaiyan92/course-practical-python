"""
Filling Up With Numbers
Write a program to fill the text file with numbers.
"""
from random import randint


try:
    file = open("file.txt", "w")
    amount = int(input())
    for i in range(amount):
        n = randint(0, 100)
        file.write(str(n) + "\n")
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    print("File written")