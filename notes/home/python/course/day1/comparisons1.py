# write a program that reads 3 values from the user
# use a condition to print if
# - all the values are different
# - 2 values are the same
# - all the values are the same

a,b,c = input('1:'),input('2:'),input('3:')

if a == b == c:
    print('All the same')
elif (a == b or
      b == c or
      c == a):
    print('Two are the same')
    # if you wish to know which pair is the same:
    if a==b:
        print('a,b the same')
    elif b==c:
        print('b,c the same')
    else:
        print('a,c the same')
else:
    print('All different')

