# string is a collections of letters:
# for can be used to loop over letters/characters of string

text = 'PYTHON'
print(f'{text=}')

for letter in text:
    print(f'{letter=}')

# write a program to calculate sum of digits 
# of all digits contained in some text (text can be inputted by user)

# iterate over each character
# if the characted is digit - convert to number and add to the sum
# finally print the sum

# to test if a character is a digit use the in operation with all possible digits in a string

digits = '0123456789'

input_data = 'Today is 19/11/2025.'

sum_of_digits = 0

for character in input_data:
    if character in digits:
        sum_of_digits += int(character)

print(f'{sum_of_digits=}')


