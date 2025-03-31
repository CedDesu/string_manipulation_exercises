"""
input

all_upper = all('A' <= c <= 'Z' for c in text if c.isalpha())

print
"""

text = input("Enter a string: ")

all_lower = all('a' <= c <= 'z' for c in text if c.isalpha())

print("Is the string all lowercase?", all_lower)
