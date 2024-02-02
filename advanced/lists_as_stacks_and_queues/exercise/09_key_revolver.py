'''
Each bullet can unlock a lock with a size equal to or larger than the size of the bullet. The bullet goes into the keyhole, then explodes, completely destroying it.
Input
•	On the first line of input, you will receive the price of each bullet – an integer in the range [0-100]
•	On the second line, you will receive the size of the gun barrel – an integer in the range [1-5000]
•	On the third line, you will receive the bullets – a space-separated integer sequence with [1-100] integers
•	On the fourth line, you will receive the locks – a space-separated integer sequence with [1-100] integers
•	On the fifth line, you will receive the value of the intelligence – an integer in the range [1-100000]
After Sam receives all of his information and gear (input), he starts to shoot the locks front-to-back while going through the bullets back-to-front.
If he successfully destroyed a lock, print "Bang!", then remove the lock. If not, print "Ping!", leaving the lock intact. The bullet is removed in both cases.
If Sam runs out of bullets in his barrel, print "Reloading!" on the console, then continue shooting. If there aren't any bullets left, don't print it.
The program ends when Sam runs out of bullets or the safe runs out of locks.
Output
•	If Sam manages to open the safe, print:
"{bullets_left} bullets left. Earned ${money_earned}"
•	Otherwise, print:
"Couldn't get through. Locks left: {locks_left}"
Make sure to include the price of the bullets when calculating the money earned.
'''
from collections import deque

price_of_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullet_size = deque(int(x) for x in input().split())
lock_size = deque(int(x) for x in input().split())
value_of_the_intelligence = int(input())

bulets = 0
while lock_size:
    if bullet_size:
        curr_bullet = bullet_size.pop()
        bulets += 1
        curr_lock = lock_size[0]
        if curr_lock < curr_bullet:
            print('Ping!')
        else:
            print('Bang!')
            lock_size.popleft()

        if (bulets % size_of_the_gun_barrel == 0) and bullet_size:
            print('Reloading!')
    else:
        print(f"Couldn't get through. Locks left: {len(lock_size)}")
        break

cost_of_bullets = bulets * price_of_bullet
earn = value_of_the_intelligence - cost_of_bullets

if not lock_size:
    print(f'{len(bullet_size)} bullets left. Earned ${earn}')