# write a basic rock-scissors-paper game

# 1.the computer generates a random move
# 2.the user enters his move
# 3.using a condition decide and display result of the game

# to represent moves use letters: r s p
# to get random move we will use function choice
# from the random module

# to use a function from module we have to import it:

from random import choice

# when you give choice a string, it will return random
# letter from it:

pc_move = choice('rsp')

user_move = input('Your move r/s/p:')

print(f'The PC moves: {pc_move}')

if pc_move == user_move:
    print('It is a draw')
elif (pc_move=='r' and user_move=='s' or
      pc_move=='s' and user_move=='p' or
      pc_move=='p' and user_move=='r'):
    print('I am winning hooray!')
else:
    print('Well, you win, congratulations or whatever')

