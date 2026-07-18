# for loop is used to iterate trhough items/elements
# of an iterable objects

# the for loop is repeated as many times as there are
# elements in the its iterable

# during each iteration 1 item is assigned to loop variable:

# for LOOP_VARIABLE in ITERABLE_OBJECT:
#       INDENTED_BLOCK

# we can simply iterate over list of values:

for var in 10,20,'thirty',40.5,20:
    print(f'{var=}\t{type(var)=}')

# first iterable object: numerical (integer) ranges
# we create a range object with the range function
# 1.option: range(start,stop)
#           creates a range <start,stop) - again
#           upper boundary IS NOT INCLUDED!
print()

r1 = range(1,5)

for item in r1:
    print(f'{item=}\t{type(item)=}')

print()
print(f'{r1=}\t{type(r1)=}')

# usually we do not assign ranges to variables
# instead we construct them directly in the for:
print()

for i in range(1,11):
    print(i)

# print the multiplication tables of numbers 1 to 10
# 1 * 1 = 1
# 1 * 2 = 2
# ...
# 4 * 10 = 40
# 5 * 1 = 5
# ...
# 9 * 10 = 90
# 10 * 10 = 100

for a in range(1,11):
    for b in range(1,11):
        # we specify the length of the fields: {field:lenght}
        print(f'{a:2} * {b:2} = {a*b:3}')











