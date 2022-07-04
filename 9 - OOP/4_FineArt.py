"""
Fine Art
Complete the program for a drawing application to print the perimeter of the rectangle.

"""
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return "Rectangle with width: " + str(self.width) + " and height: " + str(self.height)

    def draw_rectangle(self, is_rectangle):
        if is_rectangle:
            for i in range(self.height):
                if i == 0 or i == self.height - 1:
                    print("*" * self.width)
                else:
                    print("*" + " " * (self.width - 2) + "*")
        else:
            print("Not a rectangle")

    def is_rectangle(self):
        if self.width != self.height:
            return True
        else:
            return False
    
rectangle = Rectangle(int(input("Insert width rectangle: ")), int(input("Insert height rectangle: ")))
rectangle.draw_rectangle(rectangle.is_rectangle())
print("Perimeter: " + str(rectangle.perimeter()))
print("Area: " + str(rectangle.area()))