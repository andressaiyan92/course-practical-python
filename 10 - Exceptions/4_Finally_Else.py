"""
finally

After a try/except statement, a finally block can follow. 
It will execute after the try/except block, no matter if an exception occurred or not.

"""
try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Divide by zero")
finally:
    print("this code will run no matter what")

"""
El bloque finally es útil, por ejemplo, cuando se trabaja con archivos y recursos: 
se puede utilizar para asegurarse de que los archivos o recursos se cierran o se liberan 
independientemente de que se produzca una excepción.
"""
"""
else

The else statement can also be used with try/except statements.
In this case, the code within it is only executed if no error occurs in the try statement.

Example:
"""
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(2)
else:
    print(3)
"""
Run the code and see how it works!
"""