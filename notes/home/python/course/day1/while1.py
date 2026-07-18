# the while loop: repeating a block while a condition is true
# used mainly when you do not know beforehand how many times to repeat

# while CONDITION:
#       INDENTED_BLOCK

# the condition is tested on the start of each repetition
# - even on the first repetition
# and the indented block si repeated as long as the condition is True

# endless loop:
#while True:
#    print('I am repeating')

# when used with control variable we must:

i = 1       # initialize variable

while i < 5:        # have loop condition
    print(i)        # do some work in the loop

    i += 1          # modify the loop variable

print('End of loop')
print()
# while is necessary to loop until something occurs

# example: repetition of entry until user enters r/p/s

move = 'INVALID'
#while move!='r' and move!='p' and move!='s': # too cumbersome
# enhance using in operator:
# beware of text in 'string': works even for empty string ''!!!

while move not in ('r','p','s'):
    move = input('Your move r/p/s:')

print(f'The selected move is {move}.')


