"""
input

print
"""

text = input("Enter a string: ")

lowercase = ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in text)

print("Result:", lowercase)