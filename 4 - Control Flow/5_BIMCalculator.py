"""
Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. 
It’s calculated using a person's weight and height, using this formula: weight / height²

The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9

Sample Output
Normal
"""
weight = float(input("Ingresa tu peso: "))
height = float(input("Ingresa tu altura: "))
bim = weight / (height ** 2)
if bim < 18.5:
    print("Bajo de peso")
elif bim >= 18.5 and bim < 25:
    print("Normal ")
elif bim >= 25 and bim < 30:
    print("Sobrepeso")
else:
    print("Obesidad")
 