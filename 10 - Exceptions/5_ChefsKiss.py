"""
Chef's Kiss
Create a program for a digital menu which will take the index of the item
 as input and output the item name.
"""
try:
    menu = ["Pizza", "Pasta", "Salad", "Sandwich", "Burger"]
    for i in range(len(menu)):
        print(str(i + 1) + " " +  menu[i])
    index = int(input("Enter the index of the item: ")) - 1
    print(menu[index])
except IndexError:
    print("Invalid index")

try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)

"""
*************************************
"""
try:
    d = 2 + "Hola" # Si comentas esto entra en ZeroDivisionError
except Exception as ex:
    print("Ha habido una excepción", type(ex))
