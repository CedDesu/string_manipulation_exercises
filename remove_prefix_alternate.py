"""

text = input ()
prefix = input ()

use if and len to remove prefix

"""

text = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

if text.startswith(prefix):
    text = text[len(prefix):]

print("Result:", text)