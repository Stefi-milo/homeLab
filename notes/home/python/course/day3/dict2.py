# write a simple translation dictionary program

# we start with some sample data 

dictionary = {
    'red':'cervena',
    'green':'zelena',
    'blue':'modra',
}
# we will keep reading words from user until just enter is pressed

while True:
    word = input('Enter word for translation:')
    if not word:
        break
    # now if the word is a key in dictionary print translation
    # if not ask the user for the translation and append it to the dictionary
    elif word in dictionary:
        print('Translation:',dictionary[word])
    else:
        translation = input('Unknown, enter translation:')
        dictionary[word] = translation

