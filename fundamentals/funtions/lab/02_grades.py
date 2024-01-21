number_grade = float(input())
def solve(number: float) -> str:
    '''
    # function that receives float grade between 2.00 and 6.00 and prints text the corresponding grade in words.
    # •	2.00 – 2.99 - "Fail"
    # •	3.00 – 3.49 - "Poor"
    # •	3.50 – 4.49 - "Good"
    # •	4.50 – 5.49 - "Very Good"
    # •	5.50 – 6.00 - "Excellent"
    '''
    word_grade = ''

    if 2 <= number <= 2.99:
        word_grade = 'Fail'
    elif 3.00 <= number <= 3.49:
        word_grade = 'Poor'
    elif 3.50 <= number <= 4.49:
        word_grade = "Good"
    elif 4.50 <= number <= 5.49:
        word_grade = "Very Good"
    elif 5.50 <= number <= 6.00:
        word_grade = "Excellent"

    return (word_grade)


print(solve(number_grade))
