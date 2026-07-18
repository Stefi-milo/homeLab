# input and output of functions
# input: function parameters
# output: return values of function

# to define function with parameters we specify 
# their names in parenthesis in the def construct:

# when specified like this the function requires exactly this many parameters:
def addition(param1,param2):
    result = param1 + param2
    print(f'{result} = {param1} + {param2}')

# now addition requires 2 parameters:
addition(10,20)

# parameters are passed into local variables of the specified names
# print(param1) # NameError - param1 is undefined outside the function/

# python functions are automaticaly able to work with different data types
# if the code does only what is possible with the passed types:
addition('Hello','World')

# output - return value can be returne using
# return expression
# returns the expression and terminates the function body

def add_and_return(a,b):
    return a+b
    print('This code is never executed')

print()
result = add_and_return(100,200)
print(f'{result=}')
# or use return value in another function

print(f'{add_and_return([1,2],[3,4])=}')

# in python every function has a return value
# but without the return statement it is the None value
print()

return_value = addition(1,2)
print(f'{return_value=}\t\t{type(return_value)=}')

# although it is recommended to have only 1 return in function
# you can use multiple return for ex. in condition:

def even_odd(number):
    if number % 2:      # remainder after division by 2
        return 'odd'
    else:
        return 'even'

print(f'{even_odd(13)=}')

# write function distance with 2 numeric parameters
# it will return the distance of the 2 parameters

# print(distance(10,100)) -> 90
# print(distance(100,10)) -> 90

def distance(a,b):
    if a > b:
        return a-b
    else:
        return b-a

print(f'{distance(100,10)=}')
print(f'{distance(10,100)=}')

# python can easily return multiple values:
# return list,of,values -> returned as a tuple of values

# function to get integer and fractional part of a number

def number_parts(number):
    int_part = int(number)
    fract_part = number - int_part
    return int_part,fract_part

print()
result = number_parts(5.5)
print(f'{result=}')

# when you know the number of returned parameters
# you can use the multi-assignment statement to assign
# the values to individual variables
i,f = number_parts(20/3)
print(f'{i=} {f=}')
