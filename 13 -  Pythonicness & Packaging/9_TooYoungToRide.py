"""
Too Young To Ride
Write a program that breaks the loop and outputs 'Too young!' in case of finding a value less than 16.
"""
ages = [24, 18, 25, 30, 35, 16, 19, 15, 21, 28, 26]
for age in ages:
    if age < 16:
        print("Too young!" + " " + str(age))
        break
else:
    print("No more young people!")