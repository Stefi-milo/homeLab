# the if condition: control structure that controls
# the flow of the program

# if CONDITION:
#    INDENTED_BLOCK
#    must have the same level indentation
# END OF BLOCK
# must be again at the original indendation level


# in python you cannot change indentation level at will:
#a = 1
#    b = 2  # impossible

if 2 == 1:  # condition False block is skipped
    print('This is first line of block')
    print('This is second line of block')
print('This is no longer part of the block')
print()

# if statement can contain more conditions using elifs block
# and one file option using else block - all optional:

if 1 == 2:
    print('Block1')
elif 1 == 3:
    print('Block2')
elif 1 == 4:
    print('Block3')
else:
    print('No condition was true')

# if more than 1 condition using elif is True
# only the first one is executed:
print()

if False:
    print('nothing')
elif True:
    print('Block True one')
elif True:
    print('Block True two')












    
