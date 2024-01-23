# You are given a secret message you should decipher.
# To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)
def first_letar(word: list) -> str:
    leter_1 = ''
    for letter in word[::-1]:
        if 48 <= ord(letter) <= 57:
            leter_1 += letter
            word.remove(letter)
    ascii_code = int(leter_1[::-1])
    word.insert(0, chr(ascii_code))
    return word

def swich_second_last(word: list) -> str:
    if len(word) > 2:
        last_letter = word.pop()
        second_letter = word.pop(1)
        word.append(second_letter)
        word.insert(1, last_letter)
    return (''.join(word))

def decode(code_message: list) -> str:
    message = []
    for word in code_message:
        word = first_letar(list(word))
        word = swich_second_last(list(word))
        message.append(word)
    return (' '.join(message))

print(decode(input().split()))
