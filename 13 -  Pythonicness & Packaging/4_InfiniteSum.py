"""
Infinite Sum
Change the function and complete the code so that the function sums as many numbers as are input.
Output:
5
5
3

Instead of :
5
9
15
"""
# change the function
def adder(*args):
    print(sum(args))

adder(2, 3)
adder(2, 3, 4)
adder(1, 2, 3, 4, 5)
