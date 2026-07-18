
# variable = a place in memory able to store some data
# in python we create  a variable by assigning a value
# to assign: variable = value

var1 = 'a value' # assignment command

print(var1) # after assignment the var1 can be used instead of value

# variable can have their values changed

var1 = 1000  # variable can have a different type assigned

print(var1)

# names of variables:
# python is case sensitive

VAR1 = 2000

print('var1:',var1)
print('VAR1:',VAR1) # different variables

# python style guide recommends lower case letters only for variables
# exceptions: UPPER_CASE_LETTERS for constant variables

PROGRAM_VERSION = 1.0

# python3 expects all code to be written in UTF8 enconding
# utf8 can contain any national characters
# the names can contain letters from any alphabet:

e = 10
é = 20
ě = 30

print(e,é,ě)
# python style guide recommends only english letters
# in names: a-z A-Z 0-9 _ (underscore)

# name must not start with a number
# 2var = 2 # invalid name

# names starting with _ are recommended for 'private' variables
_secret = '12345'

# names starting and ending with __
# double underscored = dunder names
# special automatic variables and functions with 'magic' function

print(__file__) # the file of this program

# _ as a name: a short for 'useless variables'
# a variable necessary for structural/format reasons
# that do not have any practical use

# to get all existing variable use dir functions
print(dir())

# to destroy a variable you can use del command
del é,ě

print(dir())












