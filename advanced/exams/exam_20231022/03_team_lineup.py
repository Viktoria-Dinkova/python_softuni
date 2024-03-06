'''
Embracing diversity, forging victory.
Write a function called team_lineup that receives information about certain football players and their countries and returns a sorted result.
The function will receive a tuple of key-value pairs as arguments. The arguments will be passed as follows:
•	The following arguments will be the tuples with two elements - the first one is the player’s name (string), and the second one is the county’s name (string).
First, you need to sort the given information as stated below:
•	Sort the data by the number of players per country (descending);
•	If the player count is the same in two or more countries, sort the data by country name (alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function.
Output
•	The output should look like this:
   "{country_name}:"
   "  -{player1}"
   "  -{player2}"
   "  -{playerN}"
* Please note that there are exactly two intervals before the player’s name.
Constraints
•	Each tuple given will always contain the player’s name with its national country.
•	You will NOT receive the same player in two or more different countries.
'''


def team_lineup(*players):
    lineup = {}
    result = ''
    for player in players:
        name = player[0]
        country = player[1]
        if country not in lineup:
            lineup[country] = [name]
        else:
            lineup[country].append(name)
    for el in sorted(lineup.items(), key=lambda c: (-len(c[1]), c[0])):
        result += f"{el[0]}:\n"
        for p in el[1]: #sorted(el[1]):
            result += f"  -{p}\n"
    return result


#
#
# print(team_lineup(
#    ("Harry Kane", "England"),
#    ("Manuel Neuer", "Germany"),
#    ("Raheem Sterling", "England"),
#    ("Toni Kroos", "Germany"),
#    ("Cristiano Ronaldo", "Portugal"),
#    ("Thomas Muller", "Germany")))
