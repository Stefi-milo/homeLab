# in addition to basic range(start,stop)
# we have two more options:
# 1. range(number_of_items) - gives that many numbers starting with 0

r2 = range(5)
print(f'{r2=}')
print()

for item in r2:
    print(f'{item=}')

# in fact shortcut for range(0,number_of_items)

# try to display 3-row line of 40 * using for, range, print and string multiplication
# can be done in 2 lines of code

# when the loop variable has no other use, it is customary to use the _ as the name
# (throwaway variable - used only for the for structure)

for _ in range(3):  
    print(40*'*')

# 2. third range option: range(start,stop,step)
#    creates a range from start to stop-1 but instead of step 1
#    it will have the specified step - an integer

print()

for n in range(10,50,5):
    print(n)

# to create decreasing range you must use negative step
# and start > stop:

print()
for n in range(5,0,-1):
    print(n)
# the stop (right boundary) is again not included in the range

# use for with ranges and print with string repetition
# to display an arrow of specified lenght:

# for lenght 5:

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

max_length = 5

for n in range(1,max_length):
    print(' *' * n)
for n in range(max_length,0,-1):
    print(' *' * n)

print()
# another - more complicated but 'cleaner' solution
# loop over the ranges first:

for r in range(1,max_length),range(max_length,0,-1):
    for n in r:
        print(' #' * n)
   
