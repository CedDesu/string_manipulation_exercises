"""
text = input()
char = input()

count = 0

print()
"""

text = input("Enter a string: ")
char = input("Enter the character to count: ")

count = 0
for c in text:
    if c == char:
        count += 1

print(f"'{char}' appears {count} times in the string.")