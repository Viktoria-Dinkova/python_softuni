"""
You are given a file called numbers.txt with the following content:
'''
1
2
3
4
5
'''
Create a program that reads the numbers from the file. Print on the console the sum of those numbers.
"""
import os.path

file_path = os.path.join('texts', 'numbers.txt')
suma = 0

with open(file_path, 'r') as file:
    rows_text = file.readlines()
    suma = sum([int(n.strip()) for n in rows_text])

print(suma)