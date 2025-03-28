"""
text = input()
width = input()

center_space

print()
"""

text = input("Enter a sentence: ")
width = int(input("Enter the total width: "))

center_space = max(width - len(text), 0)
text = ' ' * (center_space // 2) + text + ' ' * (center_space - center_space // 2)

print("Result:", text)