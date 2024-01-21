# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# Write a function that receives an integer number and returns one of the following messages:
# •	"We have a perfect number!" - if the number is perfect.
# •	"It's not so perfect." - if the number is NOT perfect.
# Print the result on the console.

def perfect_number(input_number: int) -> str:
    '''
    check if the input number is perfect

        :param input_number: int

        :return message: str
    '''
    list_of_divisors =[]

    for num in range(1, input_number + 1):
        if input_number % num == 0:
            list_of_divisors.append(num)

    if sum(list_of_divisors) / 2 == input_number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")

in_num = int(input())
perfect_number(in_num)