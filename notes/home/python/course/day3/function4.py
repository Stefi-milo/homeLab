# create two functions:
# function dice that will return a 1 random number = roll of standard dice
# (import the ranrange function from random module for this)

# second function: dices with parameter how_many
# that will use the first function to fill in a list with how_many
# random rolls of a dice, and returns this list


# print(dice()) -> prints number 1...6
# print(dices(5)) -> [d,d,d,d,d] list of 5 random dice rolls

from random import randrange

def dice():
    roll = randrange(1,7)
    return roll

# use for in range loop and list.append method

def dices(how_many):
    results = []        # creating a new list
    for _ in range(how_many):
        results.append(dice())
    return results      # return the list

print(f'{dices(5)=}')

# we can make parameter of a function optional
# by specifying =value in the function definition

def example(a,b=10,c=20):
    # a is required - does not have default value
    # b and c are optional - need not to be specified
    print(f'example: {a=} {b=} {c=}')

print()
example('first')    # a is required parameter
# when you specify more than required parameters they are filled in 
# with specified values from the left
# the rest is left at default values from the right

example('first','second')
# i can specify value for all parameters
example('first','second','third')

# when defining function all required parameters
# must precede all the optional ones:

# def invalid(a=1,b): # SyntaxError
#     print()


# universal dice function: the number of sides can be specified
# but the default value is 6

def universal_dice(sides=6):
    return randrange(1,sides+1)

print()
print(f'{universal_dice()=}')
print(f'{universal_dice(100)=}')

# now we add second optional parameter to force the dice to return highest number

def cheating_dice(sides=6,cheating=False):
    if cheating:
        return sides
    else:
        return randrange(1,sides+1)

print()
print(f'{cheating_dice(6,True)=}')
print(f'{cheating_dice(100,True)=}')
# when skipping all parameters we will get standard non-cheating dice
print(f'{cheating_dice()=}')
# with 1 parameter we are specifying the number of sides withou cheating
print(f'{cheating_dice(100)=}')

# to skip an optional parameter (or to specify different order of parameters)
# we can use 'keyword call': the use of name of parameter in the call of function

print(f'{cheating_dice(cheating=True)=}')
print(f'{cheating_dice(cheating=True,sides=100)=}')

# sometimes keyword call is necessary to pass optional parameters
# to function that accept any number of parameters:

print(1,2,3,4,5,6,7,8,9) # any parameter to print is a thing to print out
# as print takes any positional parameter as value to print
# we must specify the sep=separator between items
#                     end=end line after items
# using keyword call:

print(1,2,3,4,sep='---',end='...\n\n')
print(1,2,3,4,sep='')

print('hello',end='')
print('WORLD')
