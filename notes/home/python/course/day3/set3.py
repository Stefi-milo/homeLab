# sets can perfrom set operation:
# union = items combined from multiple sets
# itersection = items common to multiple sets
# difference = items not present in other set

s1 = set(range(1,6))
s2 = set(range(3,8))

print()
print(f'{s1=}')
print(f'{s2=}')

intersection1 = s1.intersection(s2)
intersection2 = s1 & s2                 # the same operation
print(f'{intersection1=}')
print(f'{intersection2=}')

union1 = s1.union(s2)
union2 = s1 | s2
print(f'{union1=}')
print(f'{union2=}')

# try tu use difference method or - operator
# to get the difference between sets
difference1 = s1.difference(s2)
difference2 = s1 - s2
print(f'{difference1=}')
print(f'{difference2=}')
