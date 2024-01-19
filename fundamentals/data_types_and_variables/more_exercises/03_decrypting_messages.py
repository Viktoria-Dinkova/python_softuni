# On the first line, you will receive a key (integer).
# On the second line, you will receive n – the number of lines, which will follow.
# On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.

decriptor = int(input())
lines_count = int(input())
message = ''
for index in range(lines_count):
    char = ord(input()) + decriptor
    message += chr(char)

print(f'{message}')