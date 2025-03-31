"""

user input

use while and len to replace spaces with nothing

print user input
print(text[:i+1])

"""

text = input("Input a sentence: ")

i = len(text) - 1
while i >= 0 and text[i] == ' ':
    i -= 1

print(text[:i+1])
