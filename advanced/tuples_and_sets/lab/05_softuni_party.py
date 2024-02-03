'''
There is a party at SoftUni. Many guests are invited, and there are two types of them: Regular and VIP.
When a guest comes, check if they exist on any of the two reservation lists.
On the first line, you will receive the number of guests – N.
On the following N lines, you will be receiving their reservation codes. All reservation codes are 8 characters long,
and all VIP numbers will start with a digit. Keep in mind that all reservation numbers must be unique.
After that, you will be receiving guests who came to the party until you read the "END" command.
In the end, print the number of guests who did not come to the party and their reservation numbers:
•	The VIP guests must be first.
•	Both the VIP and the Regular guests must be sorted in ascending order.

'''
invited_count = int(input())
inv_vip = set()
inv_regular = set()
coming_vip = set()
coming_regular = set()

for _ in range(invited_count):
    guest = input()
    if guest[0].isdigit() == True:
        inv_vip.add(guest)
    else:
        inv_regular.add(guest)

all_inv = inv_vip | inv_regular

coming = input()
while coming and coming != 'END':

    if coming in all_inv:
        if coming[0].isdigit() == True:
            coming_vip.add(coming)
        else:
            coming_regular.add(coming)

    coming = input()

all_came = coming_vip | coming_regular
missed = all_inv - all_came

if missed:
    print(len(missed))
    print(*(sorted(missed)), sep='\n')

else:
    print(0)
    # print(*(sorted(all_inv)), sep='\n')