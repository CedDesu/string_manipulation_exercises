"""
text = input()
suffix = input()

ends_with

print()
"""

text = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

ends_with = text[-len(suffix):] == suffix if len(suffix) <= len(text) else False

print("Does the string end with the suffix?", ends_with)