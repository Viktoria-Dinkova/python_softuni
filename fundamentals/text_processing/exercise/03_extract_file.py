# Write a program that reads the path to a file and subtracts the file name and its extension.
all_path = input()
ext = all_path.split('.')
extantion = ext[1]
path = ext[0].split('\\')
name = path[len(path) - 1]

print(f'File name: {name}')
print(f'File extension: {extantion}')


