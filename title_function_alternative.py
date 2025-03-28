"""
text = input()

title_text =

print()
"""

text = input("Enter a sentence: ")

title_text = ' '.join(word[0].upper() + word[1:].lower() if word else '' for word in text.split())

print("Result:", title_text)