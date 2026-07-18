# data types in python
# typing is dynamic: types are automatically taken from the values
# a variable does not have a type - types are taken from
# contained value

# although dynamic python is a typed language:
# different types behave differently

num1 = 10       # integer value 10
txt1 = '10'     # text value 10

# printing by itself behaves the same:
print('num1:',num1)
print('txt1:',txt1)

# lets try to print double of the value
print()
print('num1+num1:',num1+num1)
print('txt1+txt1:',txt1+txt1)

# operation +: on numbers does addition
#              on strings does concatenation

# operation *: on numbers does multuplication
#              on strings does repetition

print()
print('txt1*num1:',txt1*num1)

# not all operations are available for every type
# strings support only + and *

# not all operations can taky any arguments
# string * can only use integer on the other side

# or: + is not defined for combination number and string
#num1 + txt1 # TypeError - impossible combination of operands

# to get the type of a value: use type function
# type(value) returns the type of parameter

print()
print('10:',type(10))       # int
print('"x":',type("x"))     # str
print('1.5:',type(1.5))     # float

# another basic data type is the bool = boolean value
t = True        #
f = False       # beware uppercase first lest
print(t,type(t))
print(f,type(f))

# CONVERSION - IMPLICIT/AUTOMATIC
# ONLY FOR NUMBERS: THE RESULT OF A CALCULATION
# IS ALWAYS OF THE WIDEST (MOST GENERIC) TYPE

print()

result1 = 10 + 20
result2 = 10 + 20.5

print(result1,type(result1))
print(result2,type(result2))


# the implicit conversion goes:
# bool > int > float > complex












