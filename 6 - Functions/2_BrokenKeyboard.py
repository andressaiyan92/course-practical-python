"""
Your friend sent you a message, however his keyboard is broken and types a # instead of a space.
Replace all of the # characters in the given input with spaces and output the result.
"""
msg = input()
new_message = msg.replace("#", " ")
print(new_message)