# use of sets to compare data from files

# to simply read text from files we can use Path class from pathlib module

from pathlib import Path

filename1 = 'data1.txt'
filename2 = 'data2.txt'

# to read text we can use the Path object - we create Path object for each file
file1 = Path(filename1)
file2 = Path(filename2)

# to read text contents we use the Path.read_text() method
# in windows we have to use: encoding='utf8' parameter
text1 = file1.read_text(encoding='utf8')
text2 = file2.read_text(encoding='utf8')

# we split the texts into lines by splitting on '\n' = newline
lines1 = text1.split('\n')
lines2 = text2.split('\n')

common_lines = set(lines1) & set(lines2)
print(common_lines)
