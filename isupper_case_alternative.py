"""
input


print
"""

text = input("Enter a string: ")

all_upper = all('A' <= c <= 'Z' for c in text if c.isalpha())

print("Is the string all uppercase?", all_upper)