# nested data structured - working with lists of lists

matrix1 = [ [1,2],[3,4] ]

print()
print(f'{matrix1=}')

# when indexing you get the inner structure:
print(f'{matrix1[0]=}')

# to get inner item we continue with indexing:
print(f'{matrix1[0][0]=}')

# to loop over structure we need nested for loops
# when reading data only for item in object is necessary:

product = 1
for row in matrix1:
    for item in row:
        product *= item

print(f'{product=}')

# to modify - we need to loop over using indexes:
for yi in range(len(matrix1)):
    for xi in range(len(matrix1[yi])):
        matrix1[yi][xi] *= 2

print()
print(f'{matrix1=}')

# to enter large matrixes: you can break line in any parenthesis:
print()

matrix2 = [
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10], # final comma in list is allowed - has no meaning
]

print(matrix2)

# to print big structures instead of print use 
# pprint function from the pprint module - PrettyPrinter

from pprint import pprint

pprint(matrix2)


