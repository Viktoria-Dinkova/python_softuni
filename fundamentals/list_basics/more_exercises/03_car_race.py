# Write a program that announces the winner of a car race.
# You will receive a sequence of numbers. Each number represents the time the car needs to pass through that step (the index).
# There will be two cars. The first one starts from the left side, and the other one starts from the right side.
# The middle index of the sequence is the finish line.
# Calculate the total time each racer needs to reach the finish line and print the winner with his total time (the racer with less time).
# If you have a zero in the list, you should reduce the racer's time that reached it by 20% (from his current time).
# The number of elements in the sequence will always be odd.
# Print the result in the following format "The winner is {left/right} with total time: {total_time}".

def winner_is(racers_times: list): #-> str / int:
    '''
    program that announces the winner of a car race - point start saide and total_time of the winner

        :param racers_times: list

        :return
            winner_side: str
            totsl_win_time: int
    '''
    middle = len(racers_times) // 2
    left_times = list(int(x) for x in racers_times[:middle])
    right_times = list(int(y) for y in racers_times[middle + 1 : len(racers_times) + 1])

    l_total_time = 0
    r_total_time = 0
    total_win_time = 0
    winner_side = ''

    for ltime in left_times:
        l_total_time += ltime
        if ltime == 0:
            l_total_time *= 0.8

    for rtime in right_times[::-1]:
        r_total_time += rtime
        if rtime == 0:
            r_total_time *= 0.8

    if l_total_time < r_total_time:
        winner_side = 'left'
        total_win_time = l_total_time
    else:
        winner_side = 'right'
        total_win_time = r_total_time

    print(f'The winner is {winner_side} with total time: {total_win_time:.1f}')

cars_times = list(input().split())
winner_is(cars_times)