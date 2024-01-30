# The war is in its peak, but you, young Padawan, can turn the tides with your programming skills.
# You are tasked to create a program to decrypt the messages of The Order and prevent the death of hundreds of lives.
# You will receive several messages, which are encrypted using the legendary star enigma. You should decrypt the messages, following these rules:
# To properly decrypt a message, you should count all the letters [s, t, a, r] – case insensitive
# and remove the count from the current ASCII value of each symbol of the encrypted message.
# After decryption:
# Each message should have a planet name, population, attack type ('A', as attack or 'D', as destruction) and soldier count.
# The planet name starts after '@' and contains only letters from the Latin alphabet.
# The planet population starts after ':' and is an Integer;
# The attack type may be "A"(attack) or "D"(destruction) and must be surrounded by "!" (exclamation mark).
# The soldier count starts after "->" and should be an Integer.
# The order in the message should be: planet name -> planet population -> attack type -> soldier count.
# Each part can be separated from the others by any character except: '@', '-', '!', ':' and '>'.
# Input / Constraints
# •	The first line holds n – the number of messages– integer in range [1…100];
# •	On the next n lines, you will be receiving encrypted messages.
# Output
# After decrypting all messages, you should print the decrypted information in the following format:
# First print the attacked planets, then the destroyed planets.
# "Attacked planets: {attackedPlanetsCount}"
# "-> {planetName}"
# "Destroyed planets: {destroyedPlanetsCount}"
# "-> {planetName}"
# The planets should be ordered by name alphabetically.

import re

count_message = int(input())
attacked = []
destroyed = []


def decrypt_key(in_string: str):
    decryption_key_pattern = r'(?i)[star]+'
    decryption_key = ''.join(re.findall(decryption_key_pattern, in_string))
    decryption_key_num = int(len(''.join(decryption_key)))
    return decryption_key_num


for i in range(count_message):
    current_message = input()

    key = decrypt_key(current_message)
    package_encrypted_message = ''.join([chr(ord(x) - key) for x in current_message])

    message_pattern = r'[^\@\-\!\:\>]*[@]([A-Z][a-z]+)[^\@\-\!\:\>]*[\:](\d+)[^\@\-\!\:\>]*[\!]([AD])[\!][^\@\-\!\:\>]*[\-][\>](\d+)'
    match_attack = re.match(message_pattern, package_encrypted_message)  # 'PQ@Alderaa1:30000!A!->20000'
    if match_attack:
        planet_name, planet_population, attack_type, soldier_count = match_attack.groups()  # 'Alderaa',30000, 'A', 20000

        if attack_type == 'A':
            attacked.append(planet_name)
        else:
            destroyed.append(planet_name)

print(f'Attacked planets: {len(attacked)}')
attacked = sorted(attacked)
for attacked_planet in attacked:
    print(f'-> {attacked_planet}')
print(f'Destroyed planets: {len(destroyed)}')
destroyed = sorted(destroyed)
for destroyed_planet in destroyed:
    print(f'-> {destroyed_planet}')
