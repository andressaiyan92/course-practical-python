"""
Fix the code to output the given percentage of the price.

Sample Input
50
10

Sample Output
5.0

Current code:
"""
price = int(input())
perc = int(input())

res = (lambda x,y:(x*y)/100)(price, perc)

print(res)