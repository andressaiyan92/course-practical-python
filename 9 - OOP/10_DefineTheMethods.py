"""
Define The Methods
In order to make the code work, define the Shape class, and the static area() method which 
should return the multiplication of its two arguments.
"""
class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @staticmethod
    def area(length, width):
        return length * width

print(Shape.area(10, 20))