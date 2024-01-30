# Write a program that processes information about a race.
# On the first line you will be given list of participants separated by ", ".
# On the next few lines until you receive a line "end of race" you will be given some info
# which will be some alphanumeric characters. In between them you could have some extra characters which you should ignore.
# For example: "G!32e%o7r#32g$235@!2e". The letters are the name of the person and the sum of the digits is the distance he ran.
# So here we have George who ran 29 km. Store the information about the person only if the list of racers contains the name of the person.
# If you receive the same person more than once just add the distance to his old distance.
# At the end print the top 3 racers ordered by distance in descending in the format:
# "1st place: {first racer}
# 2nd place: {second racer}
# 3rd place: {third racer}"

import re

participants = input().split(', ')#['George', 'Peter', 'Bill', 'Tom'] #input().split(', ')
race_info = {}
in_messages = []

pilot_pattern = r'[a-zA-Z]+'
score_pattern = r'[\d]'

while True:
    in_message = input()#['G4e@55or%6g6!68e!!@', 'R1@!3a$y4456@', 'B5@i@#123ll', 'G@e54o$r6ge#', '7P%et^#e5346r', 'T$o553m&6']#input()
    if in_message == 'end of race':
        break
    else:
        in_messages.append(in_message)

for message in in_messages:
    pilot = ''.join(re.findall(pilot_pattern, message))
    score = list(map(int, re.findall(score_pattern, message)))

    if pilot in participants:
        if pilot not in race_info.keys():
            race_info[pilot] = sum(score)
        else:
            race_info[pilot] += sum(score)

output = sorted(race_info.items(), key=lambda item: item[1], reverse=True)[:3] # има за довършване

print(f"1st place: {output[0][0]}")
print(f"2nd place: {output[1][0]}")
print(f"3rd place: {output[2][0]}")
