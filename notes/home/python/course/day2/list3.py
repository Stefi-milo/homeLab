# List modification methods
# list is mutable object - we can change contents and its size using methods

l1 = [10,20,30]
print(f'\n{l1=}')
# to add single item at the end of list: list.append(element)

# as list is mutable all methods that change its contents
# modify it in-place = the object on which the method is called is changed
# and usualy there is no useful return value

l1.append(40)
l1.append('ABC')
print(f'{l1=}')

# to insert item somewhere in a list you can use insert method
# list.insert(index,item) 
# it inserts new value at specified index,pushing values to the right

l1.insert(1,15)
print(f'{l1=}')
# negative indexes are allowed as well
l1.insert(-2,'DEF')
print(f'{l1=}')

# Removing items: 
# to remove item at index we can use the list.pop() method
# without parameter: removes last item
# with parameter: removes item at specified index

print()
# the removed item is returned as the returned value:
# we can assign it somewhere - but do not have to:
l1.pop()    # removes last item
removed = l1.pop(1)   # removes item for index 1

print(f'{l1=}')
print(f'{removed=}')

# use of pop and container in while loop to process data:
# we calculate sum of all numbers:
my_sum = 0
while l1:   # while the list is not true
    item = l1.pop()     # take last item
    if type(item) == int:   # if it is integer
        my_sum += item
print()
print(f'{my_sum=}')
print(f'{l1=}')         # the list is empty - it was processed fully

print()

# list.remove(item) - removes first occurence of item in list
# it is an error if item is not contained!

# to test if item is contained use item in list:

l2 = list('abeceda')
print(f'{l2=}')
l2.remove('c')
print(f'{l2=}')
# when removing item contained multiple times only 1st copy is removed:
l2.remove('a')
print(f'{l2=}')

# to remove multiple copies you can use while loop - 'remove while it is there'
while 'e' in l2:
    l2.remove('e')

print(f'{l2=}')
