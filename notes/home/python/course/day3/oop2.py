# we can define default values for object attributes using class attributes
# class attribute is shared by all instances of class
# object attribute if present shadows/covers class attribute of the same name

class BetterClass:
    # class attributes are defined here
    name = 'none'
    number = 0

b1 = BetterClass()
b2 = BetterClass()
b3 = BetterClass()

# assignin into object attribute creates local=object attribute that shadows class one
b1.name = 'A'
b1.number = 1
b2.name = 'B'
b3.number = 3

all_objects = [b1,b2,b3,BetterClass()]
print()
for item in all_objects:
    print(f'{item.name=}\t{item.number=}')

print()
# to change class attribute we must use the class object:
BetterClass.name = '(no name)'
for item in all_objects:
    print(f'{item.name=}\t{item.number=}')

