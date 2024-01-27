# Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.
sequence = input().split()
result_elements = {}
for element in sequence:
    low_element = element.lower()

    if low_element not in result_elements:
        result_elements[low_element] = 1
    else:
        result_elements[low_element] += 1

for language, count in result_elements.items():
    if count % 2 != 0:
        print(language, end=' ')

