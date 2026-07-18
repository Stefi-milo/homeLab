# use of JSON module to save and load program data to a JSON file
from json import dump,load
# using the Path from pathlib to check if a file exists
from pathlib import Path

filename = 'dictionary.json'
# we construct a Path object for the filename
savefile = Path(filename)

# does the save file exists?
if savefile.is_file():          # if true then file exists
    # loading here
    # we have to open the file usig open function
    # usualy open is used in with construct - "a context manager"
    # the context manager automaticaly handles closing the file etc.
    with open(filename,encoding='utf8') as file_object:
        # once file is opened we get the data using load function 
        dictionary = load(file_object)
        # the context manager automatically closes the file here
else:
    # file does not exist - load sample data
    dictionary = {
        'red':'cervena',
        'green':'zelena',
        'blue':'modra',
    }

while True:
    word = input('Enter word for translation:')
    if not word:
        break
    elif word in dictionary:
        print('Translation:',dictionary[word])
    else:
        translation = input('Unknown, enter translation:')
        dictionary[word] = translation

# when program ends it will always rewrite the data file using current dictionary
# we open file for writing using 'w' mode for write

with open(filename,'w',encoding='utf8') as file_object:
    # dump function will store its 1st parameter into file in 2nd parameter
    dump(dictionary,file_object)
    # file is automatically close once the with block ends

