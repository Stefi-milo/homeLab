# loop control statement: break
# terminates the closest (innermost) loop

while True:
    print('Beginning')
    break   # unconditional end of loop
    print('End')

# usually we combine break with if
# if SOMETHING:
#       break

while True:
    move = input('Move r/s/p:')
    if move in ('r','s','p'):
        # end this loop if the entry was correct
        break

print(f'Selected is {move}')

