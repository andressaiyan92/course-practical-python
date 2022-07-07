"""
Social Media Pro
Write a program for your research, that will take a text as input and return all the hashtags in it separately.
"""
"""
You are a social media marketing specialist doing research on social networks.
Write a program for your research that will take text as input and output all of the hashtags in it separately.

Sample Input
No #pressure, no #diamonds

Sample Output
#pressure
#diamonds
"""
"""
Remember that the re.findall() method returns a list of all substrings that match a pattern. So, you can use the regex r"#\w+" to find all words 
that start with a hashtag and output them on separate lines.
"""
import re

public = input("Enter a post: ")
hashtags = re.findall(r"#\w+", public)
for hashtag in hashtags:
    print(hashtag)
