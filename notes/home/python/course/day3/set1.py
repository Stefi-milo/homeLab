# set - a mutable container for unique elements
# can contain only immutable (*in fact - only hashable objects but normally immutables are hashable)
# a set does not keep order of items - therefore items are not indexed

# creating a set: {items,in,curle,braces}

s1 = { 10,20,10,20,'a','a','b' }

print(f'\n{s1=}\t\t{type(s1)=}\n')

# creation of empty set
s0 = {}

print(f'{s0=}\t\t{type(s0)=}\n')
# {} create an empty dict - not a set
# to create an empty set you have to use conversion function set()
# without any parameter: set()

s0 = set()
print(f'{s0=}\t\t{type(s0)=}\n')

# we can use the conversion function do drop duplicates 
# by converting an object with elements to a set:

l2 = [10,20,30] * 3
print(f'{l2=}')

# to get only uniques simply convert to a set
s2 = set(l2)
print(f'{s2=}')

# a set can be converted back to list if needed:
l2_unique = list(s2)
print(f'{l2_unique=}')

# example with strings in set that will randomize the order:
s3 = set('hello world hello people hello everyone'.split())
print(f'\n{s3=}')

# to get the unique words in alphabetical order we first convert to list:
l3 = list(s3)
print(f'{l3=}')

# to sort a list we can use the list.sort() method
l3.sort() # sorts the list in-place
print(f'{l3=}')

# a set is a container - can be looped over:
print()

for item in s3:
    print(f'{item=}')

# there are no indexes nor slices

# to check if there is an items you can use the in operator:
print(f'{10 in s3=}')
print(f'{"hello" in s3=}')

# to get number of items you can use len(set)
print(f'{len(s3)=}')

# as list set is a mutable type - to create a new copy of set 
# use the set.copy() method:

print()
s3_copy = s3.copy()

print(f'{s3 == s3_copy=}') # the same contents
print(f'{s3 is s3_copy=}') # the objects are differect
