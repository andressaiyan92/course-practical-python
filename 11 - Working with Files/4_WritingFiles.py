"""
Writing Files

To write to files you use the write method.

For example:    
"""
try:
    file = open("file.txt", "w")
    file.write("Writing to a file with Python")
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    print("File written")

"""
This will create a new file called "newfile.txt" and write the content to it.
In case the file already exists, its entire content will be replaced when you open it in write mode using "w".
"""

"""
If you want to add content to an existing file, you can open it using the "a" mode, which stand for "append":
"""
try:
    file = open("file.txt", "a")
    file.write("\nAppending to a file with Python")
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    print("File appended")
"""
This will add a new line with a new book title to the file.
Remember, \n stands for a new line.
"""

"""
The write method returns the number of bytes written to a file, if successful.
"""
try:
    msg = "Hello World!"
    file = open("file.txt", "a")
    amount_write = file.write("\n" + msg)
    print(amount_write)
except FileNotFoundError:
    print("File not found")
finally:
    file.close()
    print("File appended")

"""
The code above will write to the file and print the number of bytes written.
To write something other than a string, it needs to be converted to a string first.
"""