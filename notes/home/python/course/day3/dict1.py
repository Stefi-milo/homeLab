# dict - dictionary - a mutable collection of pairs of key and value
# the keys must be unique and immutable (* in fact hashable)
# the values can be anything - even mutables duplicates etc.

# the keys are used instead of indexes to look up values
# the key-value pairs are stored in the order of insertion

# empty dict

d0 = {}

# dict with items needs pairs of key:value

d1 = {10:100,'a':'ABC',(1,2):[10,20],'a':'ABCD'}
print()
print(f'{d1=}\t\t{type(d1)=}')

# dict() conversion function requires a iterable object
# that provides pairs of values for key and value
# dict([10,20,30,40]) # TypeError - impossible

# to be able to convert to list we must use a nested list for example:
d2 = dict([[10,20],[30,40]])
print(f'{d2=}')

# manipulating items of dict:
# 1. access to item: key access - just like indexing: dict[key]

print()
print(f'{d1[10]=}')
print(f'{d1["a"]=}')
print(f'{d1[(1,2)]=}')

# asking for non-present key is a KeyError
# d1['b'] # KeyError

# 2. to insert or change a value you simple assign to a key
#    dict[key] = value 
#    if present key is overwritten with new value, otherwise it is inserted

print()
print(f'{d2=}')
d2[10] = 200
d2[50] = 500
print(f'{d2=}')

# 3. to delete a key/value pair you use the del command
#    del dict[key]

del d2[30]
print(f'{d2=}')

# many container operations are the same for dict:
print()

# len returns number of pairs in a dict
print(f'Number of items of a dict: {len(d2)=}')

# to search for data use the in operator:
print(f'{10 in d2=}')  # in searches only in dict keys!
print(f'{200 in d2=}') # in does not search in values!

print()
# when looping over a dict using for loop
# it gives you loop over the dict keys:
for key in d2:
    print(key,d2[key]) # to get the value use the key access
    # we can modify the value in for loop using key access
    d2[key] += 1

print(f'{d2=}')
