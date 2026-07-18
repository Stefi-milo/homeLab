# Explicit / manual conversion of data types

# use function named as the target data type:
# str()
# bool()
# int()
# float()
# all takes 1 parameter: value to convert
# and return the value converted to the type in question
# - if possible, otherwise throw an Error

num1 = 100
txt1 = str(num1)    # conversion to str is always possible
num2 = int(txt1)    # conversion from str is possible if
                    # if it contains only numbers

print('num1:',num1*5)
print('txt1:',txt1*5)
print('num2:',num2*5)

# cannot convert non-numeric string to a number:
# int('abc123') # ValueError

# conversion from generic number to more speficic
# simply drops the extra part:

result1 = 20 / 3
result2 = int(result1)

print()
print('result1:', result1)
print('result2:', result2)

# (to perform math.rounding you can use round() instead)
rounded = round(result1)
print('rounded:',rounded)


# to get integer division you can simply use //
print('20 // 3 =',20//3)


