'''
You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from the positive.
Find the total sum of the negatives and positives, and print the following:
•	On the first line, print the sum of the negatives
•	On the second line, print the sum of the positives
•	On the third line:
o	If the absolute negative number is larger than the positive number:
	"The negatives are stronger than the positives"
o	If the positive number is larger than the absolute negative number:
	"The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.

'''
def negative_vs_positive(numbers:str):
    negative = [int(x) for x in numbers.split() if int(x) < 0]
    positive = [int(x) for x in numbers.split() if int(x) > 0]

    return sum(positive), sum(negative)

nums = input()
result = negative_vs_positive(nums)

print(f'{result[1]}\n{result[0]}')

if result[0] + result[1] > 0:
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")

