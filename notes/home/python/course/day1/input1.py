# data entry into the program
# reading keyboard input:
# input() function reads one line of data
# (data must end with the enter key)
# and returns it as its return value

# usually we assign the result into a variable
# input allows optional parameter: prompt printed to user

##data = input('Enter some data:')
##
### do something with data
##print('You entered:',data)


# write a program to calculate a sum of lengths
# of all sides of a square, given the length of one side

a = input('Enter length of one side:')
a_number = int(a)
sum_of_lengths = 4 * a_number
print('The sum of lenghts of the sides is',sum_of_lengths)

# or

print('The sum is:',4*int(a))
