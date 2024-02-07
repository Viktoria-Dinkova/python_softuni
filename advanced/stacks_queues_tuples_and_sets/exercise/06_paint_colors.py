'''
Write a program that finds colors in a string. You will be given a string on a single line containing substrings
(separated by a single space) from which you will be able to form the following colors:
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings and check if you can get any of the above colors' names. If there is only one substring left, you should use it to do the same check.
You can only keep a secondary color if the two main colors needed for its creation could be formed from the given substrings:
•	orange = red + yellow
•	purple = red + blue
•	green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary color after it is found.
When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and return them in the middle of the original string. If the string contains an odd number of substrings, you should put the substrings one position ahead.
For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye", so you should remove the last character and return them in the middle of the string: "r by yellow".
In the end, print out the list with colors in the order in which they are found.
Input
•	Single line string
Output
•	The list with the collected colors
'''
from collections import deque
string = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {
    "orange": {'red', 'yellow'},
    "purple": {'red', 'blue'},
    "green": {'yellow', 'blue'}}


out_colors = []

while string:
    front = string.popleft()
    end = string.pop() if len(string) > 0 else ''
    combine_string = {front + end, end + front}

    for cur_color in combine_string:
        if cur_color in main_colors or  cur_color in secondary_colors:
            out_colors.append(cur_color)
            break

    else:
        combine_string = front[:-1] + end[:-1]
        index = len(string) // 2
        if combine_string:
            string.insert(index, combine_string)


for k, v in secondary_colors.items():
    if k in out_colors and v not in out_colors:
        out_colors.remove(k)

print(out_colors)

