"""
Metacharacters are what make regular expressions more powerful than normal string methods.
They allow you to create regular expressions to represent concepts like "one or more repetitions of a vowel".

The existence of metacharacters poses a problem if you want to create a regular expression (or regex)
 that matches a literal metacharacter, such as "$". You can do this by escaping the metacharacters by
  putting a backslash in front of them.
However, this can cause problems, since backslashes also have an escaping function in normal Python 
strings. This can mean putting three or four backslashes in a row to do all the escaping.
To avoid this, you can use a raw string, which is a normal string with an "r" in front of it. We saw 
usage of raw strings in the previous lesson.
"""
"""
The first metacharacter we will look at is . (dot).
This matches any character, other than a new line.
"""
import re

pattern = r"gr.y"
if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")

"""
The next two metacharacters are ^ and $.
These match the start and end of a string, respectively.
Example:
"""
print("**************************************************************************")

pattern = r"^gr.y$"
if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")

"""
The pattern "^gr.y$" means that the string should start with gr, 
then follow with any character, except a newline, and end with y.
"""