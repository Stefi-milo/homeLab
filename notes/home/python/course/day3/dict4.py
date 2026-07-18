# to seach in dict values you can use DictView = a view on a part of dict
# method dict.values() returns a DictView on values
# object behaving like list with only the value part of a dict

d1 = {10:100,20:200,30:300}

print()
print(f'{d1=}')

# by default in searches only in keys:
print(f'{10 in d1=}')
print(f'{100 in d1=}')

# create a values view for searching in values
v1 = d1.values()
print(f'{v1=}\t\t{type(v1)=}')
print(f'{100 in v1=}')

# looping over dict using both key and value in for loop:
# method dict.items() provides in iteration pairs of key:value

print()
for item in d1.items():
    print(f'{item=}') # result is tuple
    # to access key or value we have to use indexing
    print(f'{item[0]=}\t{item[1]=}')

print()
# to make things easier for allow to use multiple
# loop variables in a multi-assignment just like regular =
# condition: the looped over object must provide correct number of values

for key,value in d1.items():
    print(f'{key=}\t{value=}')
    # warning as with lists you can not change value in dict 
    # by assigning to the loop variable
    value += 99

print(f'{d1=}')
