# You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order.
# Your task is to re-arrange the elements in a list so that the animal looks normal again:
# •	On the first position is the head;
# •	On the second position is the body;
# •	On the last one is the tail.

first_element = input()
second_element = input()
third_element = input()

body = []
body.append(first_element)
body.append(second_element)
body.append(third_element)

print(f'{body[::-1]}')

