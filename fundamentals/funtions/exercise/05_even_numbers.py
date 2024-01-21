# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().

def even_numbers(in_sequence: list) -> list:
    '''
    print a list of only the even numbers in received
    sequence of numbers (integers) separated by a single space
    
        :param: list
        
        :return: list
    '''
    num_in_sequence = [int(i) for i in in_sequence]

    result = list(filter(lambda x: x % 2 == 0, num_in_sequence))

    return result


sequence = list(input().split())
print(even_numbers(sequence))

