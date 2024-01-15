# Until you receive the command "END", you need to read commands on different lines.
# According to the commands, calculate the number of coffees you need to drink.
# The list of events is:
# · You have homework to do ("coding").
# · You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
# · You watch a movie ("movie").
# · If other events are present, Just ignore them!
#
# Each event can be lowercase or uppercase:
#
# · If it is lowercase, you need 1 coffee by an event.
# · If it is uppercase, you need 2 coffees by an event.
#
# In the end, print the number of coffees you will need.
# If the count has exceeded 5, just print "You need extra sleep".

command = input()
list_of_events_1 = ['coding','dog','cat','movie']
list_of_events_2 = ['CODING','DOG','CAT','MOVIE']
need = 0

while command != 'END':
    if command.lower() in list_of_events_1:
        if command in list_of_events_1:
            need += 1
        elif command in list_of_events_2:
            need += 2

    command = input()

if need > 5:
    print(f'You need extra sleep')
else:
    print(f'{need}')
