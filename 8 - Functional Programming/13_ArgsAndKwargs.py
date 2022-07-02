"""
*args
Python allows you to have functions with varying numbers of arguments.
Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. 
The arguments are then accessible as the tuple args in the body of the function.

Example:
"""
def function(name_arg, *args):
    print(name_arg)
    print(args)

function(1, 2, 3, 4, 5)

"""
The parameter *args must come after the named parameters to a function.
The name args is just a convention; you can choose to use another.
"""
"""
**kwargs (standing for keyword arguments) allows you to handle named arguments that you have not defined in advance.
The keyword arguments return a dictionary in which the keys are the argument names, and the values are the argument values.

Example:
"""
def my_funct(name_arg,*args, **kwargs):
    print(name_arg)
    print(args)
    print(kwargs)

my_funct(1, 2, 3, 4, 5, name="John", age=30)
"""
The arguments returned by **kwargs are not included in *args.
a and b are the names of the arguments that we passed to the function call.
"""
