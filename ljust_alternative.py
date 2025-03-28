"""
text = input()
width = input()

ends_with

print()
"""

text = input("Enter a string: ")
width = int(input("Enter the total width: "))

if len(text) < width:
    text = text + ' ' * (width - len(text))

print("Result:", text)