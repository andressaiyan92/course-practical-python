cubes = [i**3 for i in range(5)]
print(cubes)
print("***************************************")
evens = [i*2 for i in range(10) if i**1 % 2 == 0]
print(evens)
print("***************************************")
"""
Ignore the Vowels
Output a list that contains letters of the word that are not vowels.
"""
word = input()
not_vowels = "".join([i for i in word if i.lower() not in "aeiou"])
print( not_vowels )
"""
Data Structures

As we have seen in the previous lessons, Python supports the following collection types: Lists, Dictionaries, Tuples, Sets.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot/should not change.
Many times, a tuple is used in combination with a dictionary, for example, a tuple might represent a key, because it's immutable.
"""
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
