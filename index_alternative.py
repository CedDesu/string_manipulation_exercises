"""
text = input()
char = input()

position = -1

print()
"""

text = input("Enter a sentence: ")
char = input("Enter the character to find: ")

position = -1
for i in range(len(text)):
    if text[i] == char:
        position = i
        break

if position != -1:
    print(f"The first occurrence of '{char}' is at index {position}.")
else:
    print(f"'{char}' is not found in the user input.")