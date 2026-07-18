# advanced indexing: you can index seqeunces in backwards (from the end)
# by using negative indexes: -1 last item
#                            -2 next to last

text = 'PYTHON'
print(f'\n{text=}\n')

print(f'{text[-1]=}')
print(f'{text[-2]=}')
print(f'{text[-3]=}')
print(f'{text[-4]=}')
print(f'{text[-5]=}')
print(f'{text[-6]=}')

# SLICING = CREATING SLICES (PARTS) OF SEQUENCES
# create a slice of sequence by specifiyng start and stop point
# sequence[start:stop] - like indexing with 2 values 

print(f'\n{text=}\n      012345\n')

print(f'{text[2:5]=}')
print(f'{text[0:3]=}')
print(f'{text[1:4]=}') # as with every range, the upper boundary is not included

# to get slice up to the end we can use upper boundary length(sequence)
# = index bigger than last element
print()
print(f'{text[0:6]=}') # the complete original text
# to specify "all the way" in some direction you can simply skip the value:
print(f'{text[:3]=}')
print(f'{text[3:]=}')
# if you skip the start and the end it means from beginning to the end
print(f'{text[:]=}')

print()
print(f'{text[-3:]=}') # last 3 letters using negative indexing

# import the ascii letters and print
# first 8 letters of alphabet using slice
# last  6 letters of alphabet using slice

from string import ascii_uppercase

print(f'{ascii_uppercase[:8]=}')
print(f'{ascii_uppercase[-6:]=}')

# three parameter slice: slice with step:
# sequence[start:stop:step] 

print(f'\n{text=}\n')
print(f'{text[0:6:2]=}')
print(f'{text[1:5:3]=}')

# to get the every second letter of alphabet:
print()
# get every second from the begin to the end:
print(f'{ascii_uppercase[::2]}')
# the other half of alphabet:
print(f'{ascii_uppercase[1::2]}')

# to get backwards slice use negative step
# with negative step one must have the beginning > end:
print()

# when start < stop with negative step, the result is empty:
print(f'{text[0:6:-1]=}')
# either use start > stop:
print(f'{text[5:0:-1]=}') # 0 as right boundary is not included
# to go backwards all the way to the beginning you must skip 2.parametr
print(f'{text[5::-1]=}') 
# if you wish everything backwards simply skip first 2 parameters in slice:
print(f'{text[::-1]=}') 

# write a simple palindrome detector:
# read a word/string from user 
# detect whether it is spelled exactly the same forwards and backwards
# display result

# example: radar -> palindrome
#          barbar -> not a palindrome

candidate = input('Enter palindrom candidate:')

if candidate == candidate[::-1]:
    print('Yes it is a palindrome')
else:
    print('No not a palindrome')
