"""
Write a program that traverses a given directory for all files. Search through the first level of the directory only and
write information about each found file in report.txt. The files should be grouped by their extension. Extensions should be ordered by name alphabetically.
The files with extensions should also be sorted by name. report.txt should be saved in the chosen directory.
"""
import os.path

file = "2.py"
curr_dir = os.path.dirname(os.path.abspath(__file__))
# curr_dir = os.path.join('C:\\', 'old7v', 'TFS', 'INSTRUKCII')
files = {}

dir_content = os.listdir(curr_dir)
for file in dir_content:
    if os.path.isfile(file):
        file_name, ext = file.split('.')
        if ext not in files:
            files['.'+ext] = [file_name]
        else:
            files['.'+ext].append(file_name)

sort_files = sorted(files.items(), key=lambda item: item[0])
for s in sort_files:
    print(f"{s[0]}\n")
    for z in sorted(s[1]):
        print(f'---{z}{s[0]}')
