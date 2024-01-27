# Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
# You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.
# The cool threshold could be a huge number, so be mindful.
# An emoji is valid when:
# •	It is surrounded by 2 characters, either "::" or "**"
# •	It is at least 3 characters long (without the surrounding symbols)
# •	It starts with a capital letter
# •	Continues with lowercase letters only
# Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
# Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
# You need to count all valid emojis in the text and calculate their coolness.
# The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji.
# Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
# You need to print the result of the cool threshold and, after that take all emojis out of the text, count them and print only the cool ones on the console.
# Input
# •	On the single input, you will receive a piece of string.
# Output
# •	On the first line of the output, print the obtained Cool threshold in the format:
# "Cool threshold: {coolThresholdSum}"
# •	On the following line, print the count of all emojis found in the text in the format:
# "{countOfAllEmojis} emojis found in the text. The cool ones are:
# {cool emoji 1}
# {cool emoji 2}
# …
# {cool emoji N}"

import re

in_string = input()
emojis = []
cool_emojis = {}

def validation(text: str):
    pattern = r'(\:{2}|\*{2})([A-Z][a-z]{2}[a-z]*)\1'
    matches = re.findall(pattern, text)
    return [x[1] for x in matches]

def coolness(emoji: str):
    cool = 0
    for singh in emoji:
        cool += ord(singh)
    return cool

nums_patt = r'\d+'
nums = [int(x) for x in ''.join(re.findall(nums_patt, in_string))]
limit_cool = 1
for i in nums:
    limit_cool *= i

print(f'Cool threshold: {limit_cool}')

emojis = validation(in_string)
for element in emojis:
    emoji_points = coolness(element)
    if emoji_points > limit_cool:
        index_element = in_string.index(element)
        cool_emojis[in_string[index_element-2:index_element+2+len(element)]] = emoji_points

print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for k in cool_emojis.keys():
     print(f'{k}')
