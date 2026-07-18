# list() - conversion function: creates a list 
# from items of any iterable object

# when converting string to list:characters are made to items:
l1 = list('abcd')
print(f'{l1=}')

# converting ranges to lists:
l2 = list(range(10))
print(f'{l2=}')

# without parameter it creates an empty list
l3 = list()
print(f'{l3=}')

# operators + * += *= behave exactly as on strings:
# + combination of lists
# * repetition of list by number

l4 = l1 + l2
print()
print(f'{l4=}')

# how to create a list of 10 number 0?
l5 = [0] * 10  # a list with 0 repeated 10 times 
print(f'{l5=}')

# using conversion from range to list
# and with the operator + 
# create a list of numbers 1 to 5 and back to 1
# print the list

l6a = list(range(1,5)) # 1 ... 4
l6b = list(range(5,0,-1)) # 5 ... 1
l6 = l6a + l6b
print(f'\n{l6=}')

l7 = list(range(1,5)) + list(range(5,0,-1))
print(f'\n{l7=}')

# using += to add items to existing: the added object must be 
# another list or iterable object:

l10 = [10,20,30]
print(f'\n{l10=}')

# add items of a new list
l10 += [40,50]
print(f'{l10=}')

# the object being add does not have to be list - but it must be iterable:
l10 += 'ABC'
print(f'{l10=}')

# you can not use += to directly add a number - number is not iterable:
# l10 += 100 # TypeError - not possible like this
# you can overcome using single item list:
l10 += [100]
print(f'{l10=}')

