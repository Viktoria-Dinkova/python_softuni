"""
Write a function words_sorting which receives a different number of words.
Create a dictionary, which will have as keys the words that the function received. For each key, create a value that is the sum of all ASCII values of that key.
Then, sort the dictionary:
•	By values in descending order, if the sum of all values of the dictionary is odd
•	By keys in ascending order, if the sum of all values of the dictionary is even
Note: Submit only the function in the judge system
Input
•	There will be no input, just any number of words passed to your function
Output
•	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines

"""
def words_sorting(*words):
    dic = {}
    result = ''

    for word in words:
        asci = sum([ord(c) for c in word])
        dic[word] = asci

    if sum(dic.values()) % 2 != 0:
        for k, v in sorted(dic.items(), key=lambda item: -item[1]):
            result += f'{k} - {v}\n'
    else:
        for k, v in sorted(dic.items(), key=lambda item: item[0]):
            result += f'{k} - {v}\n'

    return result


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))
