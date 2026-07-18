# ways to import things from modules
# 1.import of specific names

from random import shuffle,choice,randrange

# all imported names can be used directly

print(choice(['Hello','Hi','Ciao']))

# 2.import of everything from a module
#   can be dangerous - not recommended in programs
#   usualy used only in python shell

d,e = 10,20
print(f'{d=}\t{e=}')

from math import *

# everything from module is available
print(f'{cos(pi)=}')

print(f'{d=}\t{e=}')
# problem: importing everything can easily conflict with
# the names of your own variables/functions

# 3. import of the entire module as an object

import math
# creates a new object in a variable with the module name

print()
print(f'{math=}\t{type(math)=}')

# now all functions in the module are available as methods of the module
# variables are available as attributes of the module object:

print(f'{math.cos(math.pi)=}')

# 4. import of the entire module with renaming

import statistics as s

print()
print(f'{s=}\t\t{type(s)=}')

print(f'{s.mean([1,2,3,4,5,6])=}')

# warning: do not name your files the same as the module they will import
# - when named the same, your file has hight priority and the module
# cannot be imported - no playing with statistics in file statistics.py!

# where modules are looked for?
# module import path is stored in the sys module in the path variable
print()

import sys
print(sys.path)
# starts with the folder of current program
# then standard library
# at the end site-packages: folder for extra installed modules

# sys.path is mutable:
sys.path.insert(0,'c:/python/companylib')
print()
print(sys.path)

# or you can set environment variabled PYTHONPATH
# if set this folder it is placed in front of sys.path
