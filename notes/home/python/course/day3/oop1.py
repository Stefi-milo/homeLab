# class = data type 
# OOP in python = defining custom classes with custom behaviour

class NameOfClass:    # customary to use CamelCase to name classes
    # indented body of the class follows
    # variables in body of class = class attributes
    # functions in body of class = class methods
    # for empty class we need empty body which is forbidden
    # we use the pass command  = do nothing
    pass

# to instantiate = create object of the class
# you call a class as a function and it returns the new object

o1 = NameOfClass()
o2 = NameOfClass()

print()
print(f'{o1=}\t{type(o1)=}')
print(f'{o2=}\t{type(o2)=}')
print()
print(f'{NameOfClass=}\t{type(NameOfClass)=}')

#  attribute = like a variable on the object or class
# as variables, attributes can be dynamic

o1.name = 'A'
o2.name = 'B'

print(f'{o1.name=}')
print(f'{o2.name=}')

objects = [o1,o2]
# use of objects in a loop
for an_object in objects:
    print(f'{an_object.name=}')

# dynamic attributes can be very dangerous - easy to forget to initialize in each object
objects.append(NameOfClass())
print()
# now we try the same loop again
for an_object in objects:
    print(f'{an_object.name=}') 
    # AttributeError for the 3rd object - does not have name attribute set!
