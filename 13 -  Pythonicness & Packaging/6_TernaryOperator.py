"""
Ternary Operator
Conditional expressions provide the functionality of if statements while using less code. 
They shouldn't be overused, as they can easily reduce readability, but they are often useful when assigning variables.
Conditional expressions are also known as applications of the ternary operator.
Example:
"""
print("*****************************************************************************")
a = 7
b = 1 if a >= 5 else 42
print(b)
"""
The ternary operator checks the condition and returns the corresponding value.
In the example above, as the condition is true, b is assigned 1. If a was less than 5, it would have been assigned 42.
Another example:
"""
print("*****************************************************************************")
status = 1
msg = "logout" if status == 1 else "login"
print(msg)
"""
The ternary operator is so called because, unlike most operators, it takes three arguments.
"""
