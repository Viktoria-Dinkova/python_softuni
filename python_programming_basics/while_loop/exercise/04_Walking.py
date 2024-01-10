# когато постигне целта си върви 10 000 стъпки да се изписва "Goal reached! Good job!" и колко стъпки повече е извървяла
# "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които е извървяла докато се прибира.
# След което, ако не е успяла да постигне целта си, на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."

all_steps = 0

while all_steps < 10000:
    text = input()

    if text == "Going home":
        last_steps = int(input())
        all_steps += last_steps
        break

    steps_per_day = int(text)
    all_steps += steps_per_day

if all_steps >= 10000:
    print(f'Goal reached! Good job!')
    print(f'{all_steps - 10000} steps over the goal!')
else:
    print(f'{10000 - all_steps} more steps to reach goal.')