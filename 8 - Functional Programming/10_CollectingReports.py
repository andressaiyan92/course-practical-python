"""
Collecting Reports
Add a decorator for the invoicing system in order to print the invoice in the required format.

You are working on an invoicing system.
The system has an already defined invoice() function, which takes the invoice number as argument and outputs it.
You need to add a decorator for the invoice() function, that will print the invoice in the following format:

Sample Input
42

Sample Output
***
INVOICE #42
***
END OF PAGE
The given code takes the invo
"""

#your code goes here
def decor(funct):
    def wrap(num):
        print("***")
        funct(num)
        print("***")
        print("END OF PAGE")
    return wrap
    

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input());