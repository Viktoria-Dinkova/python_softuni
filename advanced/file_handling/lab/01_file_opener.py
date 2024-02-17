"""
You are given a file called text.txt with the following text:
'''
This is some random line
This is the second line
And this is the third one
'''
Create a program that opens the file. If the file is found, print 'File found'. If the file is not found, print 'File not found'.
"""
import os.path

file_path = os.path.join('texts', '01_text.txt')
try:
    with open(file_path, 'r') as file:
        print('File found')
except (FileExistsError, FileNotFoundError):
    print('File not found')