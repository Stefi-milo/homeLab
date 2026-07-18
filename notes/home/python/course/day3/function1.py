# defining functions: 

def name_of_function():
    # indented block that creates the body of the function
    print('First command in function')
    print('Second command in function')

# to call functions use its name with ()
name_of_function()
name_of_function()

# everything is object here:
print(f'{name_of_function=}\t\t{type(name_of_function)=}')

# as function is a object of function assigned to variable:
second_function = name_of_function
second_function()

# this can be done with any function
tiskni = print
tiskni('Wow')

# function can be called once it is defined - 
# only after the def command is executed

# function3() # impossible to call here before definition

def function3():
    print()

# when program is contained in one file, first it must define
# all functions and after definitions some main action
# (usualy a function called main) is started

# function can contain docstring = documentation string
# simply first string constant inside the body of the function

def documented_function():
    """This is a documented function.
    This does nothing and is used only to demonstrate docstring"""
    print('Nothing')

# docstring can be displayed using help(function)
print()
print(help(documented_function))

