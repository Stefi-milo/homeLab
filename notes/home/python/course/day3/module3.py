# THIS IS A MODULE
# you can use any python code here

USEFUL_CONSTANT = 42

def greeting():
    print(f'This is a greeting from module with {USEFUL_CONSTANT=}.')

# to be able to use the module as
# a standalone program we need to 
# some action code:

# to avoid running this action code
# when the module is imported
# we must use __name__ dunder variable
# in file that is started as the main program
# it contains '__main__'
# otherwise - when this code is imported
# it contains module name

if __name__ == '__main__':
    # this is printed only when this is main program
    print('This is the module starting')
