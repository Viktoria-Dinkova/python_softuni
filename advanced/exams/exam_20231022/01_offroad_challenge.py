
'''
There will be two sequences of integers. The first sequence will represent the initial fuel and the second - additional consumption index due to thin air at high altitudes,
 hence higher fuel consumption. There will also be a third sequence of integers, representing values equal to the necessary amount of fuel needed to reach the corresponding
 altitude in the challenge.
Your task is to take the last fuel quantity from the fuel sequence and the first index from the additional consumption index sequence. Subtract the values and check the result.
•	The corresponding altitude is reached if the calculated result is bigger or equal to the first element from the needed amount of fuel sequence.
You need to remove both the fuel and the consumption index from their sequences as well as the needed amount of fuel index from their sequence.
•	If the calculated result is smaller or not equal to the first element from the needed amount of fuel sequence,
the corresponding altitude is not reached, movement cannot continue, and the program should end.
Input
•	The first line will represent the initial fuel – integers, separated by a single space.
•	The second line will represent the consumption indexes that decrease initial fuel – integers, separated by a single space.
•	The third line will represent the quantities needed to reach the corresponding altitude – integers, separated by a single space.
Output
•	On the first or the next n lines, output the corresponding message on the console from the following options:
	If John reaches the altitude, print the message:
o	"John has reached: Altitude 1"
o	…
o	"John has reached: Altitude {n}"
	If John fails to reach the altitude, print the message:
o	"John did not reach: Altitude {n}"
•	On the next lines, based on whether he reached the top or not, print the following on the console in the specified format:
	If John doesn't have enough fuel to reach the top but has reached some altitude, display the following messages:
o	"John failed to reach the top.
Reached altitudes: Altitude 1, … Altitude {n}"
	If John does not have enough fuel to reach the top and has not reached any altitude, print:
o	"John failed to reach the top.
John didn't reach any altitude."
	If John manages to reach all the altitudes, he will reach the top. End the program and print on the console the following message:
o	"John has reached all the altitudes and managed to reach the top!"

Constraints
•	All the given numbers will be valid integers in the range [1, 200].
•	All sequences always consist of four elements.
•	There will be no negative input.
'''
from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_index = deque([int(x) for x in input().split()])
needed_fuel = deque(int(x) for x in input().split())

start_range = len(initial_fuel)
point = 0
i = 0

for _ in range(len(initial_fuel)):

    curr_amount = initial_fuel[-1] - consumption_index[0]
    if curr_amount >= needed_fuel[0]:
        point += 1
        initial_fuel.pop()
        consumption_index.popleft()
        needed_fuel.popleft()
        print(f"John has reached: Altitude {point}")

    else:
        print(f"John did not reach: Altitude {point+1}")
        break


if point == start_range:
    print("John has reached all the altitudes and managed to reach the top!")

elif point == 0:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

else:
    print(f"John failed to reach the top.\nReached altitudes: Altitude ", end='')
    print(*range(1, point+1), sep=', Altitude ')
