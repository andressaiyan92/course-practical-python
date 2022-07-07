"""
Metacharacters
Some more metacharacters are * + ? { and }.
These specify numbers of repetitions.
The metacharacter * means "zero or more repetitions of the previous thing". 
It tries to match as many repetitions as possible. The "previous thing" can be a single character,
 a class, or a group of characters in parentheses.
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
The example above matches strings that start with "egg" and follow with zero or more "spam"s.
"""
"""
The metacharacter + is very similar to *, except it means "one or more repetitions", 
as opposed to "zero or more repetitions".
Example:
"""
print("**************************************************************************")
pattern = r"g+"
if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")
"""
To summarize:
* matches 0 or more occurrences of the preceding expression.
+ matches 1 or more occurrence of the preceding expression.
"""
"""
The metacharacter ? means "zero or one repetitions".
Example:

"""
print("**************************************************************************")

pattern = r"ice(-)?cream"
if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")

"""
Curly braces can be used to represent the number of repetitions between two numbers.
The regex {x,y} means "between x and y repetitions of something".
Hence {0,1} is the same thing as ?.
If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
Example:
"""
print("**************************************************************************")
pattern = r"9{1,3}$"
if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")
"""
"9{1,3}$" matches string that have 1 to 3 nines.
"""