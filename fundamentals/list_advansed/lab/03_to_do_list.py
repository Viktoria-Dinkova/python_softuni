# You will be receiving to-do notes until you get the command "End".
# The notes will be in the format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Hint
# •	Use the pop() and insert() methods.

to_do = []

while True:
    command = input()
    if command == 'End':
       break
    else:
        to_do.append(command)

to_do = sorted(to_do, key=lambda importance: int(importance.split('-')[0]))
print([acctivity.split('-')[1] for acctivity in to_do])



