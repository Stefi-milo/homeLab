# copying lists (and any mutable data types):

l1 = [10,20,30]
l2 = l1         # assignment always copies only reference = link to object
# now both l2 and l1 point to the same list object!

print()
print(f'{l1=}')
print(f'{l2=}')
print()

# lets change some list:
l1.pop()
l2.append(40)

print(f'{l1=}')
print(f'{l2=}')
print()

# when working with mutables - we must take care to copy reference 
# or data - if we want a new object with the same contents we need to create
# a new copy: all standard mutable objects have object.copy()
# returns a new copy of the object with same data

l3 = l1.copy()  # l3 is now a new copy of the object

print()
print(f'{l1=}')
print(f'{l2=}')
print(f'{l3=}')

# to test object identity = if two objects are the same, use is operator:
print()
print(f'{l1 == l2=}\t{l1 is l2=}')
print(f'{l1 == l3=}\t{l1 is l3=}')
# == compares contents of objects
# is compares identity of objects

l1.pop()
print()
print(f'{l1=}')
print(f'{l2=}')
print(f'{l3=}')
