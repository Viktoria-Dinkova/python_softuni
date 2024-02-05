'''
Write a program that finds the longest intersection. You will be given a number N.
 On each of the next N lines you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}".
 You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.
Finally, you should find the longest intersection of all N intersections, print the numbers
that are included and its length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}"
Note: in each range, there will always be an intersection. If there are two equal intersections, print the first one.
'''
all_intersections = []

for _ in range(int(input())):
    first_interval, second_interval = [intervals.split(',') for intervals in input().split('-')]

    set_one = set(range(int(first_interval[0]), int(first_interval[1]) + 1))
    set_two = set(range(int(second_interval[0]), int(second_interval[1]) + 1))

    intersection = set_one & set_two
    all_intersections.append(intersection)
#
max_len = len(all_intersections[0])
for i in all_intersections:
    if len(i) > max_len:
        max_i = i

print(f'Longest intersection is [', (*max_i, sep=", "), '] with length {len(max_i)}')


# lengths = [len(x) for x in all_intersections]
# max_el = [y for y in all_intersections if (len(y) == max(lengths)) == True]
# output = [*max_el[0]]
# print(f'Longest intersection is {output} with length {max(lengths)}')

#
# count_of_inputs = int(input())
#
# all_intersections = []
#
# for _ in range(count_of_inputs):
#     info = input().split()
#     for x in info:
#         intervals = x.split('-')
#         first_interval = intervals[0].split(',')
#         first_start = int(first_interval[0])
#         first_end = int(first_interval[1])
#         second_interval = intervals[1].split(',')
#         second_start = int(second_interval[0])
#         second_end = int(second_interval[1])
#
#         set_one = {x for x in range(first_start, first_end + 1)}
#         set_two = {x for x in range(second_start, second_end + 1)}
#         intersection = set_one & set_two
#         all_intersections.append(intersection)
#
# lengths = [len(x) for x in all_intersections]
# max_el = [y for y in all_intersections if (len(y) == max(lengths)) == True]
# output = [*max_el[0]]
# print(f'Longest intersection is {output} with length {max(lengths)}')
