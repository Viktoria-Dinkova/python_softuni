"""
Create a program that creates a file called my_first_file.txt. In that file, write a single line with the content: 'I just created my first file!'
"""
import os.path

file_path = os.path.join( 'texts', 'my_first_file.txt')

with open('my_first_file.txt', 'w+') as my_file:
    my_file.write('I just created my first file!')
    my_file.seek(0)
    text = my_file.read()
    print(text)