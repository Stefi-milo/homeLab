# set modification methods:

# to add an item: set.add(item)
# adds the item if not already present, else nothing happens

# to remove an item: set.discard(item)
# removes the item if present, else nothing happens

s1 = set()
print()
print(f'{s1=}')

s1.add('abc')
s1.add('abc')
s1.add('def')
s1.add('def')

print(f'{s1=}')

s1.discard('def')
s1.discard('def')
s1.discard('xyz')

print(f'{s1=}')

# there is a counting version of set (multiset/bag)
# it is the Counter type from the collections module

from collections import Counter
#the counter behaves similat to dictionary - it counts the number of items
c1 = Counter()
c1['abc'] += 1
c1['abc'] += 1
c1['abc'] += 1

print(c1)

# counter can be also initialized from an iterable object to count occurences:
c2 = Counter('hello everyone')
print(c2)
c3 = Counter([10,20,30]*3+[10,20,10])
print(c3)
