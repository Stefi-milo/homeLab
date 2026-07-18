# formatting the text output (usually for print)

a = 10
b = 20

# to display the result of some operation

print(a,'+',b,'=',a+b)

# we can improve using formatted string / f-string
# an f-string is a text constant with the f letter in front

print(f'this is an f-string') # no difference from regular string

# in a f-string variable and expression are interpolated
# inside {curly braces}

print(f'a is {a} and b is {b}')

# expression can be evaluated as well

print(f'{a}+{b}={a+b}')

print()

# expression can contain even function calls:

print(f'a is of type {type(a)} and has value {a}')

# debug output: display of automatic label for an expression:
print()

# to use debug output put = at the end of expression:
#  {expression=}

print(f'{a=} {b=} {a+b=}')

print(f'{type(str(a+b))=}')


# you cannot ask for a undefined variable
##print(f'{c=}') # NameError










