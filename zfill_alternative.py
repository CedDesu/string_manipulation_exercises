"""
text = input()
width = input()

if len(text) < width:
    text = '0' * (width - len(text)) + text

print()
"""


text = input("Enter a sentence: ")
width = int(input("Enter the total width: "))

if len(text) < width:
    text = '0' * (width - len(text)) + text

print("Result:", text)