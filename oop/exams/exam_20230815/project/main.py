"""
1.	Class BaseEquipment
In the base_equipment.py file, the class BaseEquipment should be implemented. It is a base class for any type of equipment, and it should not be able to be instantiated.
Structure
The class should have the following attributes:
•	protection: int
o	The value represents the protection of the equipment.
•	price: float
o	The value represents the price of the equipment.
Methods
__init__(protection: int, price: float)
•	In the __init__ method, all the needed attributes must be set.
increase_price()
•	Method increases the equipment’s price. Keep in mind that each type of equipment implements the method differently.
2.	Class KneePad
In the knee_pad.py file, the class KneePad should be implemented. The knee pad is a type of equipment. Each knee pad equipment has a protection of 120 and a price of 15.0 EUR.
Methods
__init__()
•	In the __init__ method, all the needed attributes must be set.
increase_price()
•	The method increases the price by 20% (twenty percent).
3.	Class ElbowPad
In the elbow_pad.py file, the class ElbowPad should be implemented. An elbow pad is a type of equipment. Each elbow pad has a protection of 90 and a price of 25.0 EUR.
Methods
__init__()
•	In the __init__ method, all the needed attributes must be set.
increase_price()
•	The method increases the price by 10% (ten percent).
4.	Class BaseTeam
In the base_team.py file, the class BaseTeam should be implemented. It is a base class for any type of team, and it should not be able to be instantiated.
Structure
The class should have the following attributes:
•	name: str
o	The value represents the name of the team.
o	If the name is an empty string or contains only white spaces, raise a ValueError with the message: "Team name cannot be empty!"
•	country: str
o	The value represents the country of origin of a team. It should be at least 2 symbols long (no leading or trailing white spaces counts).
o	If the team’s country is less than 2 symbols long, raise a ValueError with the message: "Team country should be at least 2 symbols long!"
•	advantage: int
o	The value represents the advantage in points that each team has.
o	If the team’s advantage is less than or equal to 0, raise a ValueError with the message: "Advantage must be greater than zero!"
•	budget: float
o	The value represents the team’s budget.
•	wins: int
o	The value represents the team’s wins, initially set to 0.
•	equipment: list
o	Empty list that will contain equipment(objects) each team has.
Methods
__init__(name: str, country: str, advantage: int, budget: float)
•	In the __init__ method, all the needed attributes must be set.
win()
•	Increases the team’s advantage and the number of wins. Keep in mind that each type of team implements the method differently.
get_statistics()
The method returns the statistics about the team in the following format, each line on a new row:
"Name: {team_name}
Country: {team_country}
Advantage: {team_advantage} points
Budget: {team_budget}EUR
Wins: {number_of_wins}
Total Equipment Price: {total_price_of_team_equipment}
Average Protection: {avg_team_protection}"
•	The budget and the total equipment price should be formatted to the second decimal places.
•	Average Protection refers to the property protection of each piece of equipment that the team has in its equipment collection. Round the average protection to the smaller integer.
5.	Class OutdoorTeam
In the outdoor_team.py file, the class OutdoorTeam should be implemented. The outdoor team is a type of team. Each outdoor team has an initial budget of 1000.0 EUR.
Methods
__init__(name: str, country: str, advantage: int)
•	In the __init__ method, all the needed attributes must be set.
win()
•	The method increases the team’s advantage by 115 points. Remember to increase the wins number as well.
6.	Class IndoorTeam
In the indoor_team.py file, the class IndoorTeam should be implemented. The indoor team is a type of team. Each indoor team has an initial budget of 500.0 EUR.
Methods
__init__(name: str, country: str, advantage: int)
•	In the __init__ method, all the needed attributes must be set.
win()
•	The method increases the team’s advantage by 145 points. Remember to increase the wins number as well.
7.	Class Tournament
In the tournament.py file, the class Tournament should be implemented. It will contain the functionality of the project.
Structure
The class should have the following attributes:
•	name: str
o	The value represents the name of the tournament.
o	The name should contain letters and digits only. If the name has other symbols, raise a ValueError with the message: "Tournament name should contain letters and digits only!"
•	capacity: int
o	The number of teams а Tournament can have.
•	equipment: list
o	Empty list that will contain all equipment (objects) that are created.
•	teams: list
o	Empty list that will contain all teams (objects) that are created.
Methods
__init__(name: str, capacity: int)
•	In the __init__ method, all the needed attributes must be set.
add_equipment(equipment_type: str)
The method creates equipment of the given type and adds it to the equipment collection.
•	If the equipment’s type is not valid, raise an Exception with the following message:
"Invalid equipment type!"
•	Otherwise, create the equipment, add it to the equipment list, and return the following message:
"{equipment_type} was successfully added."
•	Valid types of equipment are: "KneePad" and "ElbowPad"
add_team(team_type: str, team_name: str, country: str, advantage: int)
The method creates a team of the given type and adds it to the teams’ collection.
All teams’ names will be unique.
•	First, check if the team type is valid, and if not raise an Exception with the following message:
"Invalid team type!"
•	Then, check if there is an available tournament capacity, and if not return the following message:
"Not enough tournament capacity."
•	Otherwise, create the team, add it to the teams’ list, and return the following message:
"{team_type} was successfully added."

•	Valid types of teams are: "OutdoorTeam" and "IndoorTeam".
sell_equipment(equipment_type: str, team_name: str)
The method adds the equipment of the given type to the team’s equipment collection. Both equipment and team will always exist.
•	First, check if the equipment can be sold to the team. If the team’s budget is not enough to buy the equipment, raise an Exception with the following message:
"Budget is not enough!"
•	If the equipment can be sold to the team, remove it from the tournament's equipment collection, and add it to the team’s equipment collection. Decrease the budget with the equipment’s price. Return the following message:
"Successfully sold {equipment_type} to {team_name}."
o	Take the last equipment of the given type from the collection.
remove_team(team_name: str)
The method removes the team with the given name from the tournament.
•	First, check if there is a team with the given name in the team’s collection. If not, raise an Exception with the following message:
"No such team!"
•	Then, check if the team has any wins. If so, raise an Exception with the following message:
"The team has {number_of_wins} wins! Removal is impossible!"
•	If the team can be removed successfully, remove it from the tournament, and return the following message: "Successfully removed {team_name}."
increase_equipment_price(equipment_type: str)
The method increases the price for all equipment of the given type that is in the tournament’s equipment collection. The equipment type will be one of the valid types (KneePad or ElbowPad). When all prices for the given equipment type are successfully changed (hint: use increase_price() method), return the following message:
"Successfully changed {number_of_changed_equipment}pcs of equipment."
o	Equipment that is already sold to teams should not be affected.
play(team_name1: str, team_name2: str)
The method starts a game between two teams. The team’s names will always exist and will be unique.
•	First, check if both teams are from one and the same type (IndoorTeam or OutdoorTeam). If not, raise an Exception with the following message:
"Game cannot start! Team types mismatch!"
•	Then, sum the points of advantage and the total protection for each team. You will need to compare the results:
o	The team with the greater result (the sum of advantage points and total protection) wins. You have to increase the winner’s points of advantage and the number of wins. You can use the team’s win() method. Return the following message:
"The winner is {team_name_of_winner}."
o	In case the teams happen to be with equal results, return the following message:
"No winner in this game."
get_statistics()
Returns information about the tournament and the teams in the tournament, sorted by number of wins, descending. Each on a new line. Use the team’s get_statistics() method.
"Tournament: {tournament_name}
Number of Teams: {number_of_teams}
Teams:
{team1_statistics}
"""

from project.tournament import Tournament

t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())


"""
KneePad was successfully added.
ElbowPad was successfully added.
OutdoorTeam was successfully added.
OutdoorTeam was successfully added.
Not enough tournament capacity.
Successfully sold KneePad to Spartak.
Successfully removed Levski.
OutdoorTeam was successfully added.
Successfully changed 1pcs of equipment.
Successfully changed 0pcs of equipment.
The winner is Spartak.
Tournament: SoftUniada2023
Number of Teams: 2
Teams:
Name: Spartak
Country: BG
Advantage: 365 points
Budget: 985.00EUR
Wins: 1
Total Equipment Price: 15.00
Average Protection: 120
Name: Lokomotiv
Country: BG
Advantage: 250 points
Budget: 1000.00EUR
Wins: 0
Total Equipment Price: 0.00
Average Protection: 0
"""