"""
input

lowercase = ''.join(chr(ord(c) + 32) if 'A' <= c <= 'Z' else c for c in text)
= upper = all('A' <= c <= 'Z' for c in text if c.isalpha())

print
"""