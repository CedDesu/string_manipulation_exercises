"""
text = input()
width = input()

if len

print()
"""

text = input("Enter a string: ")
width = int(input("Enter the total width: "))

if len(text) < width:
    text = text + ' ' * (width - len(text))

print("Result:", text)