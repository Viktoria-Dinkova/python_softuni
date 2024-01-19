# On the first line, you will receive a single number n.
# On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:
# •	even_list
# •	odd_list
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even_list). Finally, print the result.

numbers_of_line = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []
command = ''

dict = dict(even=even_list, odd=odd_list, positiv=positive_list, negativ=negative_list)

for num in range(numbers_of_line):
    curr_num = int(input())
    if curr_num >= 0:
        positive_list.append(curr_num)
    else:
        negative_list.append(curr_num)

    if curr_num %2 == 0:
        even_list.append(curr_num)
    else:
        odd_list.append(curr_num)

dict['even'] = even_list
dict['odd'] = odd_list
dict['negative'] = negative_list
dict['positive'] = positive_list

command = input()

print(f'{dict.get(command)}')