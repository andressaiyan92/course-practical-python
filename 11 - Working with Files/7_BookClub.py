"""
Book Club
Create a program which will output how many words each title of a book contains, in the provided format.
"""
try:
    file = open("books.txt", "r")
    for line in file:
        print(len(line.split(" ")))
    print("File read")
except FileNotFoundError:
    print("File not found")
finally:
    file.close()