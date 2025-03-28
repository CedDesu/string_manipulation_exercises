"""

user input

use while and len to replace spaces with nothing

print user input

"""

text = input("Input a sentence: ")

i = 0
while i < len(text) and text[i] == ' ':
    i += 1

print(text[i:])