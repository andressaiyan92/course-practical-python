"""
Spelling Backwards
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H
"""
def spell(txt):
    if len(txt) == 0:
        return
    else:
        print(txt[-1])
        spell(txt[:-1])
    

txt = input()
spell(txt)
