"""
Working with Files

It is good practice to avoid wasting resources by making sure that files are always closed after 
they have been used. One way of doing this is to use try and finally

"""
try:
    file = open("file.txt", "w")
    file.write("Writing to a file with Python")
    print("File written")
except FileNotFoundError:
    print("File not found")
finally:
    file.close()

"""
This ensures that the file is always closed, even if an error occurs.
"""

"""
An alternative way of doing this is by using with statements.
This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement.

"""
try:
    with open("file.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")
"""
The file is automatically closed at the end of the with statement, even if exceptions occur within it.
"""

