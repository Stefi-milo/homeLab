# List = container for any objects
# a sequence like a string = is indexed, ordered (items keep position)
# unlike string: is mutable, we can change items
# is dynamic, can grow/shrink at will

# creating: [objects,in,square,brackets]

l1 = [10,20,'thirty',20,[1,2],30.5]

print(f'\n{l1=}\t{type(l1)=}\n')

# an empty list
l0 = []

print(f'\n{l0=}\t{type(l0)=}\n')

# all accessing items - indexes,slices,for loop - are the same 
# in any sequence - the same as in string:
print(f'{l1[0]=}') # first item
print(f'{l1[-1]=}') # last item
print(f'{l1[::-1]=}') # entire list in reverse order
print(f'{len(l1)=}') # the length of list

# start with list of numbers:
numbers = [10,20,30,40]
# iterate over this list and print the items using loop
print(f'\n{numbers=}\n')

for item in numbers:
    print(item)
    item += 1   # this does not change the item in list!

# unlike string here list is mutable: we can overwrite/change items
numbers[0] = 15
print(f'\n{numbers=}\n')
# you can only overwrite values for existing indexes!

# increase each item in list by 1 using for loop
# then print the complete lists
# to write into list items we need to use the for in range(len()) loop:

for i in range(len(numbers)):
    numbers[i] += 1 # this works

print(f'\n{numbers=}\n')

