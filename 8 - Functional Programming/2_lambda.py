"""
Creating a function normally (using def) assigns it to a variable with its name automatically.
Python allows us to create functions on-the-fly, provided that they are created using lambda syntax.

This approach is most commonly used when passing a simple function as an argument to another function. 
The syntax is shown in the next example and consists of the lambda keyword followed by a list of arguments, 
a colon, and the expression to evaluate and return.
"""
def my_func(f, arg):
  return f(arg)


print(my_func(lambda x: 2*x*x, 5))


"""
Functions created using the lambda syntax are known as anonymous.
"""
"""
Lambda functions aren't as powerful as named functions.
They can only do things that require a single expression -- usually equivalent to a single line of code.
"""
#named function
def polinomial(x):
    return x**2  + 5*x + 4
print(polinomial(-4))

#lambda
print((lambda x: x**2  + 5*x + 4)(-4))
