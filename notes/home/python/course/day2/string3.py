# string as an object
# everythink in python is object
# every object belongs to its class
# each class defines some methods
# method = like a function but available only for objects of its class

# str.upper() / str.lower() - methods to convert string to upper/lowercase

# to call a method you use: object.method(parameters)

text = 'Python'

# str.upper/str.lower return the string on which they are called
# converted to specific case:

text_upper = text.upper()
text_lower = text.lower()

print()
print(f'{text=}')
print(f'{text_upper=}')
print(f'{text_lower=}')
print()

# you do not have to assign return value to a variable:
# you can even call methods on constant values of the appropriate class:
print('this is a constant value'.upper())

# Information about class methods:
# 1. Documentation: 
#    python.org > Documentation > Reference Library > Specific Type > Methods

# 2. Intellisense: suggestion of method named when writing
#    after writing object. the VS Code and similar IDEs 
#    suggest a list of all methods of the specific object

# 3. built in function help: returns documentation for given class
#    print(help(str))

# selection of string methods:
# comparison methods - detecting the contents of the string:

# str.isdigit() - returns True if string consist only of digits
print(f'{"123".isdigit()=}')
print(f'{"12X".isdigit()=}')

# str.isupper() - returns True if string consist only of uppercase
# str.islower() - the same for lowercase
# str.isalpha() - True if str.consists only of letters
# str.isspace() - True if str.consistr of spaces,tabs,newlines only

data = '123xyz'
# is the first character number?
print(f'{data[0].isdigit()=}')
# are the last 2 characters letters?
print(f'{data[-2:].isalpha()=}')

# METHODS TO CHANGE CONTENTS OF THE STRING
# str.upper()
# str.lower()

# str.replace(search_for,replace_with) - replaces all occurences 
#   of 1st parameter with the 2nd

# str.center(width) - returns string centered on specified line width
#   with one parameter using space as padding

# str.strip() - remove spaces from the beginning and the end

# ALL METHODS THAT SHOULD CHANGE CONTENTS
# ALWAYS RETURN THE CHANGED CONTENTS AS ITS RETURN VALUE:
# - NEVER CHANGE THE STRING OBJECT ON WHICH THEY ARE CALLED

print()
print(f'{text=}')
text.upper()
print(f'{text=}')
text.center(40)
print(f'{text=}')

# REASON: string (together with int,float,bool and others)
# belong IMMUTABLE objects: we nor python itself can not change
# contents of an object once created:

text = 'Python3' # a new object is created and assigned to same variable
# we cannot change part of existing object

# text[-1] = '2' # TypeError  - cannot be done, str does not support changing its items

# no method can change immutable object such as string
# therefore all changing must create a new changed copy and return it
# as its return value: usualy we need to assign the returned copy to a variable

text_upper2 = text.upper() # a new variable with changed copy created
# if you do not neet the original even the original variable can be
# used to store the changed copy

text = text.lower()

print()
print(f'{text=}')
print(f'{text_upper2=}')

# use the methods upper, replace, center
# to change the string 'python' into upper case version
# centered on line width 40
# with all spaces replaced with -

print()
text = 'python'
result1 = text.upper()
result2 = result1.center(40)
result = result2.replace(' ','-')

print(result)

# we can chain method call if they returns still the same type - here str class:
better_result = text.upper().center(40).replace(' ','-')
print(better_result)

