# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a sorted list of numbers in ascending order. Use sorted().

def sort_numbers(in_list: list) -> list:
    '''
    sort sequence of integer numbers

        :param in_list: list

        :return out_list: list
    '''
    num_input_list = [int(num) for num in in_list]

    out_list = sorted(num_input_list)

    return out_list


input_list = list(input().split())
print(sort_numbers(input_list))