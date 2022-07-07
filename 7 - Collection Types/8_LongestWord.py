"""
Longest Word


Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
Recall the split(' ') method, which returns a list of words of the string.
"""
text = input()
array = text.split(' ')
longest = ""
for word in array:
    longest = word if len(word) > len(longest) else longest
print(longest)