numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
print("***************************************")
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)
print("***************************************")
"""
Square Up
Make a function that will take the side length of a square as its argument and return the perimeter and area, using a tuple.
"""
def square_up(side):
    return (side * 4, side * side)
side = input()
print(square_up(int(side)))
