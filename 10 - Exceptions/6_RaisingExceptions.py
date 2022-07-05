"""
You can throw (or raise) exceptions when some condition occurs.
For example, when you take user input that needs to be in a specific format, 
you can throw an exception when it does not meet the requirements.
This is done using the raise statement.
"""
try:
    num = 102
    if num > 100:
        raise ValueError
except ValueError:
    print("ValueError")
"""
You need to specify the type of the exception raised. In the code above, we raise a ValueError.
"""
"""
Exceptions can be raised with arguments that give detail about them.
"""
try:
    name = "123"
    raise NameError("Invalid name")
except NameError as ex:
    print(ex)
"""
This makes it easier for other developers to understand why you raised the exception.
"""