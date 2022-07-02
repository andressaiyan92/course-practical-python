"""
Decimal to Binary
Fix the code so that it can convert its argument from decimal to binary.
"""
def dec_to_bin(num):
    bin = str(num % 2)
    if num > 1:
        return dec_to_bin(num // 2) + bin
    return bin
num = int(input())
print(dec_to_bin(num))
"""
Test
"""
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))