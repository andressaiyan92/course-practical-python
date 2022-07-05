"""
Reading Through
Make a program which will read the given number of characters of a file.
"""
try:
    file = open("file.txt")
    total_characters = 0
    for line in file:
        total_characters += len(line)
    print(total_characters)
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
