# You are a pro MOBA player, you are struggling to become а master of the Challenger tier. So, you carefully watch the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number. You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present,
# else add his position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# •	If they got at least one position in common, the player with better total skill points wins and the other is demoted from the tier -> remove him.
# •	If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
# •	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". At that point you should print the players, ordered by total skill in descending order, then ordered by player name in ascending order. For each player print their position and skill, ordered descending by skill, then ordered by position name in ascending order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Player and position will always be one word string, containing no whitespaces.
# •	Skill will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	The program ends when you receive the command "Season end".
# Output
# •	The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}
# …
# - {positionN} <::> {skill}"

moba = {}
gamesters = {}

while True:
    info = input()
    if info == 'Season end':
        break
    elif ' -> ' in info:
        info = info.split(' -> ')
        player = info[0]
        position = info[1]
        skills = int(info[2])
        if player not in moba:
            moba[player] = {position: skills}
        elif position not in moba[player]:
            moba[player][position] = skills
        elif moba[player][position] < skills:
            moba[player][position] = skills
    elif ' vs ' in info:
        info = info.split(' vs ')
        first_player = info[0]
        second_player = info[1]

        if first_player in moba and second_player in moba:
            for pos in moba[first_player]:
                if pos in moba[second_player]:
                    if moba[first_player][pos] > moba[second_player][pos]:
                        moba.pop(second_player)
                    elif moba[first_player][p] < moba[second_player][pos]:
                        moba.pop(first_player)

for k,v in moba.items():
    total_points = sum(x for x in v.values())
    gamesters[k] = total_points

gamesters = sorted(gamesters.items(), key=lambda rank: rank[1], reverse=True)
for i in gamesters:
    print(f'{i[0]}: {i[1]} skill')
    sorted_skill = {}
    for x,y in moba[i[0]].items():
        sorted_skill = sorted(moba[i[0]].items(), key=lambda can: can[1], reverse=True)
    for c, d in sorted_skill:
        print(f'- {c} <::> {d}')




