# The rules: Two teams, named "A" and "B" have 11 players each.
# The players on each team are numbered from 1 to 11.
# Any player may be sent off the field by being given a red card.
# If one of the teams has less than 7 players remaining, the referee stops the game immediately,
# and the team with less than 7 players loses.
# The card is a string with the team's letter ("A" or "B") followed by a single dash and the player's number. e.g.,
# the card "B-7" means player #7 from team B received a card.
# The task: You will be given a sequence of cards (could be empty),
# separated by a single space. You should print the count of remaining players on
# each team at the end of the game in the format: "Team A - {players_count}; Team B - {players_count}".
# If the referee terminated the game, print an additional line: "Game was terminated".
# Note for the random tests: If a player who has already been sent off receives another card - ignore it.

tim_a = []
tim_b = []
players = []

count_a = 11
count_b = 11

for i in range(1, 12):
    tim_a.append(f'A-{i}')
    tim_b.append(f'B-{i}')

players = input().split()

for player in players:

    if player in tim_a:
        tim_a.remove(player)
        count_a -= 1
    elif player in tim_b:
        tim_b.remove(player)
        count_b -= 1

    if count_a < 7 or count_b < 7:
        print(f'Team A - {len(tim_a)}; Team B - {len(tim_b)}')
        print('Game was terminated')
        break
else:
    print(f'Team A - {len(tim_a)}; Team B - {len(tim_b)}')