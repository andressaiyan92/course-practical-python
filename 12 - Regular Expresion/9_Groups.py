"""
Groups
A group can be created by surrounding part of a regular expression with parentheses.
This means that a group can be given as an argument to metacharacters such as * and ?.
Example:
"""
import re

pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
   print("Match 1")

if re.match(pattern, "eggspamspamegg"):
   print("Match 2")

if re.match(pattern, "spam"):
   print("Match 3")


"""
(spam) represents a group in the example pattern shown above.
"""
"""
The content of groups in a match can be accessed using the group function.
A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.
Example:
"""
print("**************************************************************************")
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())

"""
There are several kinds of special groups.
Two useful ones are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. 
They behave exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.
Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to 
an existing regular expression without breaking the numbering.
Example:

"""
print("**************************************************************************")
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())


"""
Another important metacharacter is |.
This means "or", so red|blue matches either "red" or "blue".
Example:
"""
print("**************************************************************************")
pattern = r"gr(a|e)y"
match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")

