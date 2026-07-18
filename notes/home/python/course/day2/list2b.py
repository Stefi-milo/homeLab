# how to create an alphabet in random order?
# import shuffle - function to randomly reorder an list

from random import shuffle
from string import ascii_uppercase

alphabet = list(ascii_uppercase)
print()
print(alphabet)
shuffle(alphabet)
print(alphabet)
