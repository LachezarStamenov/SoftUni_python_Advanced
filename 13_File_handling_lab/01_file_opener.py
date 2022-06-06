# You are given a file called text.txt with the following text:

file_path = 'text.txt'
try:
    open(file_path, 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')
