# string as a container of characters
# we can iterate through characters in string = string has items
# in a sequence with items we can acces items directly

# to access an item of a sequence we use indexing: 
# accessing item of an index -using [index] index in square brackets

text = 'PYTHON'

print(f'\n{text=}\n')

# in python all indexing always start with 0

print(f'{text[0]=}')
print(f'{text[1]=}')
print(f'{text[2]=}')
print(f'{text[3]=}')
print(f'{text[4]=}')
print(f'{text[5]=}')

# accessing index bigger than last one is an IndexError
# text[6] # IndexError

# to get the length of any sequence use the len(object) functions
# len returns number of items in the object given 

print(f'\n{len(text)=}\n')

# often len is combined with single parameter range
# to iterate over items using indexes:

for index in range(len(text)):
    # as range starts with 0 and ends with len-1 
    # we will get all existing indexes automatically:
    print(f'{index=}\t{text[index]=}')

# import alphabet from string

from string import ascii_uppercase # ASCII table contains only english letters

print(f'\n{ascii_uppercase=}\n')

# using for loop with range and indexes, 
# print every second letter and its position
# start with letter A

for i in range(0,len(ascii_uppercase),2):
    print(i+1,ascii_uppercase[i])


