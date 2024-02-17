"""
Create a program that deletes the file you created in the previous task. If you try to delete the file multiple times, print the message: 'File already deleted!'.
"""
import os.path


try:
    file_path = os.path.join('my_first_file.txt')
    os.remove('file_path')
except:
    print('File already deleted!')
