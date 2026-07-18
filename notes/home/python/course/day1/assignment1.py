# python allow multiple assignment with 1 statement:

# 1. one value to multiple variables

# all variables set to same values

x = y = z = 0

print(f'{x=} {y=} {z=}')

# the same as
x = 0
y = 0
z = 0

# 2. many values to many variables
#    the same number of values and variables
#    we assign list of values to list of variables

a,b,c = 10,20,30

print(f'{a=} {b=} {c=}')

# using this you can for example swap values of variables

a,c = c,a
print(f'{a=} {b=} {c=}')


# AUGMENTED ASSIGNMENT = CHANGE OF CURRENT VALUE OF VARIABLES

# to change current value you can read, modify and store:

print()
print(f'{x=}')
x = x + 1
print(f'{x=}')

# to write augment.assign. we skip second variable and
# flip = and operator:

x += 1
print(f'{x=}')

# augmented assignment works for every operator:
x *= 10
print(f'{x=}')

x //= 2
print(f'{x=}')

# using augmented assignment change the value of
text = 'Python'
# to the result: Python!Python!Python!
text += '!'
text *= 3

print(text)












