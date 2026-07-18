# control programs we need to evaluate logical conditions
# result of logical condition: True of False / bool values

# most often we use comparison operators:

print(f'{10 > 5=}')
print(f'{10 <= 5=}')

# for size > or < you can usually compare only same types:
#10 > 'a' # TypeError - incomparable types

# numbers are comparable
print(f'{10 > 9.9=}')
# comparisons have lower priority than arithmetic
# calculations can be compared without parentheses:

print(f'{5*2 > 3*3=}')

# comparison for equality: ==

print(f'{"hello" == "hello"=}')

# python is case sensitive even for comparing strings
print(f'{"hello" == "Hello"=}')

# different data types are different:
print(f'{10 == "10"=}')

# the exception is numbers: when numerically the same
# data type is ignored - for numbers only!
print(f'{10 == 10.0=}')

# inequality - something is differet: !=
print()

print(f'{10 != "10"=}')
print(f'{10 != 10.0=}')

# testing containment = something is inside something
# in operator: can be used with containers (tomorrow) and string
print()

print(f'{"py" in "python"=}')
print(f'{"yp" in "python"=}')

# python can compare more than 2 values
print()
print(f'{1+1 == 2 == 4//2 == int("2")=}')
print(f'{1+1 == 2 == 4//2 == int("3")=}')

# works even for > <
print(f'{10 < 20 < 30 < 40=}')
print(f'{10 < 20 < 30 < 30=}')

# to combine more logical operations together
# use logical operators:
#   and     - all of conditions must be true
#   or      - at least one of the condition must be true
#   (not)


print(f'''
{True and True=}
{True and False=}
{False and True=}
{False and False=}
''')

print(f'''
{True or True=}
{True or False=}
{False or True=}
{False or False=}
''')

print(f'''
{not True=}
{not False=}
''')






















