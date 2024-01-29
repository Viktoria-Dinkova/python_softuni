# The lottery is exciting. However, checking a million tickets for winnings only by hand is not. So, you are given the task of creating a program that automatically checks if a ticket is a winner.
# You are given a collection of tickets separated by commas and spaces (one or many). You need to check each ticket to see if it has a winning combination of symbols:
# •	A valid ticket has exactly 20 characters.
# •	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at least 6 times in both halves of the tickets.
# •	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by commas and one or more white spaces in the format:
# •	"{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# •	If the ticket is invalid: "invalid ticket"
# •	If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# •	If the ticket is valid and winning, but not a Jackpot:
import re

in_tickets = input()
lottery_tickets = in_tickets.replace(' ', '').split(',')

win_patt = r'[@#$\^]{6}'
jackpot_patt = r'[@#$\^]{10}'

for current_ticket in lottery_tickets:
    if len(current_ticket) == 20:
        first_half = current_ticket[0 : 10]
        second_half = current_ticket[10 : 21]

        if re.search(jackpot_patt, current_ticket) and re.search(jackpot_patt, current_ticket):
            print(f'ticket "{current_ticket}" - 10{current_ticket[5:6]} Jackpot!')
        elif re.search(win_patt, first_half) and re.search(win_patt,second_half):
            print(f'ticket "{current_ticket}" - 6{current_ticket[5:6]}')
        else:
            print(f'ticket "{current_ticket}" - no match')

    else:
        print('invalid ticket')
