# Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
# The input will be provided as a single string.
text = input()

for char in range(len(text) - 1):
    output = ''
    if text[char] == ':':
        output += text[char]
        output += text[char + 1]
        print(f'{output}')
