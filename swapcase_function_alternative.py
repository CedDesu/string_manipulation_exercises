"""
input

lowercase = ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in text)
= upper = all('A' <= c <= 'Z' for c in text if c.isalpha())

print
"""

text = input("Enter a sentence: ")

swapcase_text = ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else chr(ord(c) - 32) if 'a' <= c <= 'z' else c for c in text)

print("Result:", swapcase_text)