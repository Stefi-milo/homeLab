# write a program that reads data from user
# until the input is just enter (empty string/blank line)

# the data read from user should be put into list
# if the line consist only of digits, put it at the front/beginning of list
# otherwise put the line at the end of list

# when the input is only enter ('') break the loop
# print the resulting list

data = []

while True:
    line = input('Enter data,enter for exit:')
    if not line:        # when line is empty or: line == ''
        break
    # otherwise do your stuff here
    elif line.isdigit():
        data.insert(0,line)
    else:
        data.append(line)

print(data)




