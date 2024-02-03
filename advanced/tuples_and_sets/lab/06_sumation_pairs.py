'''
The task is not included in the Judge system.
You will receive a sequence of numbers (unique integers) separated by space on the first line. On the second line,
you'll receive a target number. Your task is to find the pairs of numbers whose sum equals the target number.
For each found pair print "{number} + {number} = {target_number}". You should NOT use the same element twice to fulfill the condition above.
Can you come up with an algorithm that has less time complexity?
'''
import time
from collections import deque
sequence = deque(map(int,input().split()))
target = int(input())

out = set()

strat_time = time.time()

# while sequence:
#     for i in range(len(sequence)-1):
#         next_num = i + 1
#         if sequence[0] + sequence[next_num] == target:
#             out.add((sequence[0], sequence[next_num]))
#     sequence.popleft()
#
# for tup in out:
#     num_one, num_two = tup
#     print(f'{num_one} + {num_two} = {target}')

while len(sequence) > 1:
    for i in range(1,len(sequence)):
        next_num_index = -(i+1)
        if sequence[-1] + sequence[next_num_index] == target:
            out.add((sequence[-1], sequence[next_num_index]))
    sequence.pop()

for tup in out:
    num_one, num_two = tup
    print(f'{num_one} + {num_two} = {target}')

end_time = time.time()
print(end_time - strat_time)