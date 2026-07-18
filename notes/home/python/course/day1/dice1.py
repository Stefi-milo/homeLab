# write a program that will print
# the rolls of standard dice (1...6)
# as many times until the number 6 is printed


# use the randrange function from the random module

from random import randrange

# randrange(from,to) gives you a random integer
# from the from to the to-1 !!!
# to parameter is never returned - the range si open at the top
# <from,to)


counter = roll = 0

while roll != 6:
    counter += 1
    roll = randrange(1,7)
    print(counter,roll)


# variant with break in a condition:
# how many rolls between specific number of 6 one after another:
##sixes = int(input('How many sixes in a row?'))

sixes = 3
counter = series = 0

while True:
    counter += 1
    roll = randrange(1,7)
    if roll == 6:
        series += 1
    else:
        series = 0
    if series == sixes:
        break

print(f'{counter} roll were needed to roll {sixes} series of 6')
