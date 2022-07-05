"""
Title Encoder
You are given a file named "books.txt" with book titles, each on a separate line.
To encode the book titles you need to take the first letters of each word in the title and combine them.
For example, for the book title "Game of Thrones" the encoded version should be "GoT".

Complete the program to read the book title from the file and output the encoded versions, each on a new line.
You can use the .split() method to get a list of words in a string.
"""
try:
    with open("booksencode.txt") as file:
        for line in file:
            words = line.split()
            encoded = ""
            for word in words:
                encoded += word[0]
            print(encoded)
except FileNotFoundError:
    print("File not found")

try:
  print(1)
  print(20 / 0)
  print(2)
except ZeroDivisionError:
  print(3)
finally:
  print(4)
