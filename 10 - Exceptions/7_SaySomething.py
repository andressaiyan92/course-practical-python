"""
Say Something
Complete the program so that the length of the tweet doesn't exceed 42 characters.
"""
try:
    tweet = input("Enter a tweet: ")
    if len(tweet) > 42:
        raise Exception("Tweet is too long")
    print(tweet)
except Exception as ex:
    print(ex)