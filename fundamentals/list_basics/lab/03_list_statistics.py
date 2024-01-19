# On the first line, you will receive a number n.
# On the following n lines, you will receive integers. You should create and print two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally, print the following message:
# "Count of positives: {count_positives}
# Sum of negatives: {sum_of_negatives}"

numbers = int(input())

positives = []
negatives = []

for curr_num in range(numbers):
    num = int(input())
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)

count_positives = len(positives)
sum_of_negatives = sum(negatives)
#for neg_num in range(len(negatives)):
#    sum_of_negatives += negatives[neg_num]

print(f'{positives}\n{negatives}\nCount of positives: {count_positives}\nSum of negatives: {sum_of_negatives}')
