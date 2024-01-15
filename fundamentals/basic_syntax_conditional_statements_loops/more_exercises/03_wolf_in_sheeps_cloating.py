# Warn the sheep in front of the wolf that it is about to be eaten.
# Remember that you are standing at the front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    4      3            2      1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". Otherwise, return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.

animals = list(input().split(', '))

if animals.index('wolf') + 1 == len(animals):
    print(f'Please go away and stop eating my sheep')
else:
    sheep_number = len(animals)- animals.index('wolf') - 1
    print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf! ')

