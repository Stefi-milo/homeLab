# variable scope: areas where variables are available
# all variables so far were global (module)
# = variables available in the complete file (=module)

a = 1 # global/module variable

# global variables are available for functions in the same file as well
# but by default only for reading:

def test1():
    print(f'In function: {a=}')

test1()

# by assigning into a variable in a function we create a local variable
# one that is visible only in this function - not outside
# the global a is 'shadowed' by this local a in the function:
def test2():
    a = 2
    print(f'In function2: {a=}')

test2()
print(f'Outside function2: {a=}')

# it is less confusing and recommended not to use the same
# names for local and global variables

# to write into global variable you can declare a name in a function as global:
def increase_a():
    global a
    a += 1      # working on global variable a

def set_a_10():
    global a
    a = 10      # working on global variable a

print()
print(f'{a=}')
increase_a()
print(f'{a=}')
set_a_10()
print(f'{a=}')

# it is better and safer not to write into global variables!
# easy to lose track which function modifies what values