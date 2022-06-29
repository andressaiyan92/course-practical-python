""""
******************************************************************
* When you go out to eat, you always tip 20% of the bill amount. *
*  But who’s got the time to calculate the right tip             * 
*  amount every time? Not you that’s for sure!                   *
*  You’re making a program to calculate tips and save some time. *
*                                                                *
* Your program needs to take the bill amount as input            *
* and output the tip as a float.                                 *
*                                                                *
* Sample Input                                                   *
* 50                                                             *
*                                                                *
* Sample Output                                                  *
* 10.0                                                           *
******************************************************************
"""
# Take the bill amount as input
bill = float(input("Ingrese el monto de la cuenta: $"))
# Calculate the tip
tip = (bill * 20) / 100
# Output the tip
print("Propina: $" + str(tip))