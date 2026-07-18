# methods connecting list and string:

# str.split - splitting strings into list of smaller strings
# str.join  - joining list of strings into one bigger strings

# str.split() - called on the string we wish to split into parts
# returns a list of strings (the parts)
# - without parameters: splits on spaces, tabs, newlines
# - with parameter: splits on the passed text parameter

text1 = 'python is a great language'
words1 = text1.split()

print()
print(f'{text1=}')
print(f'{words1=}')

text2 = '10,20,30,40'
data2 = text2.split(',')

print()
print(f'{text2=}')
print(f'{data2=}')

# when separator is not found, no split is performed 
# the returned list contains only one element
data3 = text2.split(';')
print(f'{data3=}')

# to combine list of string into one we call str.join method
# the join needs to be called on glue string = text that will be
# put in between each pair of items:

glue = ';'
result2 = glue.join(data2)  # call join on glue string and pass the list as parameter
print()
print(f'{result2=}')

# the glue strint does not need to be stored in a variable:
result1 = '---'.join(words1)
print(f'{result1=}')

# the glue can be even a blank string:
# to get alphabet in random order:
from random import shuffle
from string import ascii_uppercase
alphabet = list(ascii_uppercase)
shuffle(alphabet)

random_alphabet = ''.join(alphabet)
print()
print(random_alphabet)





