# Create a function that receives three parameters, calculates a result depending on the given operator, and returns it.
# Print the result of the function. The input comes as three parameters – an operator as a string and two integer numbers.
# The operator can be one of the following:  "multiply", "divide", "add", "subtract".

input_operator = input()
number_1 = int(input())
number_2 = int(input())

def calculation(operation: str, operand_1: int, operand_2: int) -> int:
    result = 0

    if operation == 'multiply':
        result = operand_1 * operand_2
    elif operation == 'divide':
        result = int(operand_1 / operand_2)
    elif operation == 'add':
        result = operand_1 + operand_2
    elif operation == 'subtract':
        result = operand_1 - operand_2
    else:
        print('Wrong operation')

    return (result)

print(calculation(input_operator, number_1, number_2))



