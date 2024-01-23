# You are a facility manager at a large business center.
# One of your responsibilities is to check if each conference room in the center has enough chairs for the visitors.
# On the first line, you will be given an integer n representing the number of rooms in the business center.
# On the following n lines for each room, you will receive information about the chairs in the room and the number of visitors.
# Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors at the end.
# For example: "XXXXX 4" (5 chairs and 4 visitors).
# Keep track of the free chairs:
# •	If there are not enough chairs in a specific room, print the following message:
#       "{needed_chairs_in_room} more chairs needed in room {number_of_room}". The rooms start from 1.
# •	Otherwise, print:
#       "Game On, {total_free_chairs} free chairs left".

rooms = int(input())
total_free_chairs = 0
for room in range(1, rooms + 1):
    note = input().split()
    free_chairs = len(note[0]) - int(note[1])
    total_free_chairs += free_chairs
    if free_chairs >= 0:
        continue
    else:
        print(f'{abs(free_chairs)} more chairs needed in room {room}')
else:
    if total_free_chairs >= 0:
        print(f'Game On, {total_free_chairs} free chairs left')





