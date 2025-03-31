"""

text = input ()
prefix = input ()

use if and len to remove suffix

"""

text = input("Enter a sentence: ")
suffix = input("Enter the suffix to remove: ")

if text.endswith(suffix):
    text = text[:-len(suffix)]

print("Result:", text)