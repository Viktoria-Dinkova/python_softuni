'''
White a function called sorting_cheeses that receives keywords arguments:
•	The key represents the name of the cheese
•	The value is a list of quantities (integers) of the pieces of the given cheese
The function should return the cheeses and their pieces' quantities sorted by the number of pieces of a cheese kind in descending order.
If two or more cheeses have the same number of pieces, sort them by their names in ascending order (alphabetically).
 For each kind of cheese, return their piece quantities in descending order.
For more clarifications, see the examples below.
'''
def sorting_cheeses(**kwargs):
    result = ''
    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for cheese, quantity in sorted_kwargs:
        result += cheese + '\n'
        for q in sorted(quantity, reverse=True):
            result += f'{q}\n'

    return result

