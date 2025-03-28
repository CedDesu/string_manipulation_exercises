"""
text = input()

capitalized_text =

print()
"""

text = input("Enter a sentence: ")

capitalized_text = (text[0].upper() + text[1:].lower()) if text else ""

print("Result:", capitalized_text)