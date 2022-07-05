"""
Reading Files
The contents of a file that has been opened in text mode can be read using the read method.
We have created a books.txt file on the server which includes titles of books.
 Let's read the file and output the content:
"""
try:
    books = open("books.txt")
    content = books.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    books.close()
"""
This will print all of the contents of the file.
"""

"""
To read only a certain amount of a file, you can provide the number of bytes to read as an argument to the read function.
Each ASCII character is 1 byte:
"""
print("\n*********************************************************\n")
try:
    books = open("books.txt")
    content = books.read(5)
    print(content)
    content = books.read(7)
    print(content)
    content = books.read()
    print(content)
except FileNotFoundError:
    print("File not found")
finally:
    books.close()
"""
This will read the first 5 characters of the file, then the next 7.
Calling the read() method without an argument will return the rest of the file content.
"""
"""
To retrieve each line in a file, you can use the readlines() method to return a list 
in which each element is a line in the file.
For example:
"""
print("\n*********************************************************\n")
try:
    books = open("books.txt")
    i = 1
    for line in books.readlines():
        print(str(i) + " - " + line)
        i += 1
except FileNotFoundError:
    print("File not found")
finally:
    books.close()

"""
If you do not need the list for each line, you can simply iterate over the file variable:
"""
print("\n*********************************************************\n")
try:
    books = open("books.txt")
    for line in books:
        print(line)
except FileNotFoundError:
    print("File not found")
finally:
    books.close()

"""
In the output, the lines are separated by blank lines, as the print function automatically 
adds a new line at the end of its output.
"""