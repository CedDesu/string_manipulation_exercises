"""
text = input()
suffix = input()

starts_with

print()
"""

text = input("Enter a sentence: ")
prefix = input("Enter the prefix to check: ")

starts_with = text[:len(prefix)] == prefix if len(prefix) <= len(text) else False

print("Does the string start with the prefix?", starts_with)