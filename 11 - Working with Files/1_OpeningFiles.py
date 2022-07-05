"""
Opening Files

You can use Python to read and write the contents of files.
This is particularly useful when you need to work with a lot of data that is saved in a file.
For example, in data science and analytics, the data is commonly in CSV (comma-separated values) files.

Let's start by working with text files, as they are the easiest to manipulate.
Before a file can be edited, it must be opened, using the open function.
"""
#import os
try:
    myfile = open("file.txt")
    # print(os.path.abspath(os.getcwd()))
except FileNotFoundError:
    print("File not found")
"""
The argument of the open function is the path to the file. If the file is in the current 
working directory of the program, you can specify only its name.
"""
"""
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).

"""
try:
    # write mode
    open("filename.txt", "w")

    # read mode
    open("filename.txt", "r")
    open("filename.txt")

    # binary write mode
    open("filename.txt", "wb")
except FileNotFoundError:
    print("File not found")

"""
You can combine modes, for example, wb from the code above opens the file in binarywrite mode.
"""
"""
Once a file has been opened and used, you should close it.
This is done with the close method of the file object.
"""
try:
    file = open("filename.txt", "w")
    # do stuff to the file
    file.close()
except FileNotFoundError:
    print("File not found")

"""
We will read/write content to files in the upcoming lessons.
"""    