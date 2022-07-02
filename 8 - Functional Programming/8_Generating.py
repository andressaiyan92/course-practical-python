"""
Generating...
Create a generator function that will take two numbers as 
arguments and output the prime numbers in the provided range.
"""
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def numbers(min, max):
    for i in range(min, max):
        if is_prime(i):
            yield i

listNumbers = list(numbers(5, 10))
print(listNumbers)
