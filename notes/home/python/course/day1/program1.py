# hash sign starts a line comment
# there are no block comments

1+1 # nothing is printed here
# unlike python shell python program does not print results automatically

# to print anything we use the print function
# to run the print function we call it using ()

print() # this way only a new line is printed

# to print out something we pass the things to print
# as 'parameters' inside the parenthesis

print(1+1)

# print function accepts any number of parameters
# = things to print, separated with commas:

print(1,2,3,4,5) # by default items are separated with space in the printout

# to enter text (a string) we must use 'apostrophes'
# or "double quotes"

print('hello',"world")

# to write text with ' or " use the other quotation mark:
print('"Murder", she wrote.')

# you can prefix a character in a text using \backslash
# \' \" in any string is just a ' or "
# \n    new line
# \t    tab character

print('\'apostrophes\'\ttab\nnewline')

# to write multi-line texts using \n
print('\nfirst\nsecond\nthird')

# to write multi-line text easily you can put it in
# ''' three apostrophes '''
# or """ three double quotes """

print('''
first
second
third
''')

# generally one command must be on 1 line of source code
# exceptions: multi-line texts
#             line-breaks inside parenthesis

print(
    1+
    2+
    3
)









