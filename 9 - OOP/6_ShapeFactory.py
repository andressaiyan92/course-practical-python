"""
Shape Factory
Improve the drawing application so that it can support adding and comparing two Shape objects.
"""
class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __ne__(self, other):
        return not self == other

    def draw_shape(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print("*" * self.width)
            else:
                print("*" + " " * (self.width - 2) + "*")

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height

rectangle = Shape(10, 5)
square = Shape(5, 5)
square.draw_shape()
rectangle.draw_shape()
print("Perimeter rectangle: " + str(rectangle.perimeter()))
print("Area rectangle: " + str(rectangle.area()))
print("Perimeter square: " + str(square.perimeter()))
print("Area square: " + str(square.area()))