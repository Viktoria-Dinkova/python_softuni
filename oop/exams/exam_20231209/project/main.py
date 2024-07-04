"""
1.	Class BaseFish
In the base_fish.py file, the class BaseFish should be implemented. It is a base class for any type of fish, and it should not be able to be instantiated.
Structure
The class should have the following attributes:
•	name: str
o	The value represents the name of the fish.
o	If the name is an empty string or contains only white spaces, raise a ValueError with the message: "Fish name should be determined!"
•	points: float
o	Represents the points a fish will bring to the diver, based on the type of fish.
o	Must be a value between 1 and 10, both inclusive. If not, raise a ValueError with the message: "Points should be a value ranging from 1 to 10!"
•	time_to_catch: int
o	The value represents how many seconds a diver requires to catch the fish.
Methods
__init__( name: str, points: float, time_to_catch: int)
•	In the __init__ method, all the needed attributes must be set.
fish_details()
•	Returns a string with information about the fish depending on its type.
•	Keep in mind that each type of fish implements the method.
2.	Class PredatoryFish
In the predatory_fish.py file, the class PredatoryFish should be implemented. A predatory fish is a type of fish. Each predatory fish has a time to catch of 90 seconds.
Methods
__init__(name: str, points: float)
•	In the __init__ method, all the needed attributes must be set.
fish_details()
•	Provide information about the PredatoryFish in the following format:
"{type of fish}: {name} [Points: {points}, Time to Catch: {time_to_catch} seconds]"
3.	Class DeepSeaFish
In the deep_sea_fish.py file, the class DeepSeaFish should be implemented. A deep-sea fish is a type of fish. Each deep-sea fish has a time to catch of 180 seconds.
Methods
__init__(name: str, points: float)
•	In the __init__ method, all the needed attributes must be set.
fish_details()
•	Provide information about the DeepSeaFish in the following format:
"{type of fish}: {name} [Points: {points}, Time to Catch: {time_to_catch} seconds]"
4.	Class BaseDiver
In the base_diver.py file, the class BaseDiver should be implemented. It is a base class for any type of divers, and it should not be able to be instantiated.
Structure
The class should have the following attributes:
•	name: str
o	The value represents the name of the diver.
o	If the name is an empty string or contains only white spaces, raise a ValueError with the message: "Diver name cannot be null or empty!"
•	oxygen_level: float
o	Represents the diver's oxygen level remaining, in seconds.
o	If the oxygen level is less than 0, raise a ValueError with the message:
"Cannot create diver with negative oxygen level!"
•	catch: list
o	It will store a sequence of fish, caught by a specific diver.
•	competition_points: float
o	Represents the total points accumulated by a diver, based on the type of fish caught during the competition. Set the initial value of the property to zero. Returns a floating-point number rounded to the first decimal place.
•	has_health_issue: bool
o	The property indicates if the diver has potential health concerns. Its initial value is False, representing that the diver starts in a healthy state.
Methods
__init__(name: str, oxygen_level: float)
•	In the __init__ method, all the needed attributes must be set.
miss(time_to_catch: int)
•	Decreases the diver's oxygen_level property. When the method is invoked the diver's oxygen_level is decreased by a certain value, that will depend on the fish that is chased.
•	Keep in mind that each type of diver can implement the method differently.
renew_oxy()
•	The diver's oxygen_level should be fully replenished to its original value. This would mean setting the oxygen_level back to its starting value depending on the diver’s type.
•	Keep in mind that each type of diver has a different level of oxygen and it will implement the method differently.
hit(fish: BaseFish)
•	The method takes a fish parameter. This fish represents the target fish that the diver is trying to catch. The method performs the following actions:
o	The diver's oxygen_level is reduced by the duration specified by the time_to_catch property of the given fish. It's important to note that the oxygen level should not drop below 0. If the diver's oxygen level is less than the time required to catch the fish, you should set the diver's oxygen_level to 0.
o	Only if the diver's oxygen_level is sufficient to catch the fish should it be added to the diver's catch list.
o	If the fish is caught, the diver's competition_points increase by the value of the points property of the caught fish, rounded to one decimal place.
update_health_status()
•	Changes the health status of the diver to True, if it is False or reciprocally.
__str__()
•	Returns a string with information about the Diver in the format below.
"{type of diver}: [Name: {name}, Oxygen level left: {oxygen_level}, Fish caught: {count of caught fish}, Points earned: {competition_points}]"
5.	Class FreeDiver
In the free_diver.py file, the class FreeDiver should be implemented. The free diver is a type of diver. Each diver has an initial oxygen level value of 120.
Methods
__init__(name: str)
•	In the __init__ method, all the needed attributes must be set.
miss(time_to_catch: int)
•	This method reduces the diver's oxygen_level by 60% of the time_to_catch value of the missed fish. If the calculated value is not a whole number, it is rounded to the nearest whole integer. Additionally, it ensures that the oxygen level does not fall below 0. If the diver's current oxygen level is insufficient to catch the fish, the method sets the diver's oxygen_level to 0, preventing it from going into negative values.
renew_oxy()
•	Restoring the oxygen_level to its original value for divers of this type.
6.	Class ScubaDiver
In the scuba_diver.py file, the class ScubaDiver should be implemented. The scuba diver is a type of diver. Each diver has an initial oxygen level value of 540.
Methods
__init__(name: str)
•	In the __init__ method, all the needed attributes must be set.
miss(time_to_catch: int)
•	This method reduces the diver's oxygen_level by 30% of of the time_to_catch value of the missed fish. If the calculated value is not a whole number, it is rounded to the nearest whole integer. Additionally, it ensures that the oxygen level does not fall below 0. If the diver's current oxygen level is insufficient to catch the fish, the method sets the diver's oxygen_level to 0, preventing it from going into negative values.
renew_oxy()
•	Restoring the oxygen_level to its original value for divers of this type.
7.	Class NauticalCatchChallengeApp
In the nautical_catch_challenge_app.py file, the class NauticalCatchChallengeApp should be implemented. It will contain the functionality of the project.
Structure
The class should have the following attributes:
•	divers: list
o	An empty list to store all diver objects assigned for the competition.
•	fish_list: list
o	An empty list for storing all fish objects that are allowed for chasing in the competition.
Methods
__init__()
•	In the __init__ method, all the needed attributes must be set.
dive_into_competition(diver_type: str, diver_name: str)
The method creates a diver of the given type and adds it to the divers collection.
•	If the diver’s type is not valid, return the following message:
"{diver_type} is not allowed in our competition."
•	If a diver with the same name is already added to the list, do not duplicate records, return the following message:
"{diver_name} is already a participant."
•	If none of the above cases is reached, the diver is successfully created. Store the diver in the appropriate collection and return it:
"{diver_name} is successfully registered for the competition as a {diver_type}."
•	Valid types of divers are: "FreeDiver" and "ScubaDiver"
swim_into_competition(fish_type: str, fish_name: str, points: float)
The method creates a fish of the given type and adds them to the fish collection. The method is responsible for allowing a new fish to chase into the competition.
•	First, check if the fish type is valid, and if not, return the following message:
"{fish_type} is forbidden for chasing in our competition."
•	Then, check if the fish name is already added to the list, do not duplicate records, and return the following message:
"{fish_name} is already permitted."
•	If the above case is not reached, create the correct type of fish and add it to the appropriate collection. Return the following message:
"{fish_name} is allowed for chasing as a {fish_type}."
•	Valid types of fish are: "PredatoryFish" and "DeepSeaFish".
chase_fish(diver_name: str, fish_name: str, is_lucky: bool)
The method is responsible for allowing the specific diver to chase and attempt to catch a specific fish:
•	Diver Validation:
o	Validates the existence of a diver with the given diver_name in the collection of registered divers.
o	If no diver is found, the method returns the message:
"{diver_name} is not registered for the competition."
•	Fish Validation:
o	Validates the existence of a fish with the given fish_name in the list of allowed fish.
o	If no fish is found, the method returns the message:
"The {fish_name} is not allowed to be caught in this competition."
•	Health Check:
o	Checks if the diver has a has_health_issue equal to True then returns the message:
"{diver_name} will not be allowed to dive, due to health issues."
•	Oxygen Level Comparison:
o	If the diver’s oxygen_level is less than the fish's time_to_catch value, the fish escapes, the diver misses with the harpoon, and the method returns:
"{diver_name} missed a good {fish_name}."
o	If the diver's oxygen_level is equal to the fish's time_to_catch:
	If is_lucky is True, the diver successfully catches the fish by invoking the hit method with the targeted fish and return the relevant message:
"{diver_name} hits a {points}pt. {fish_name}."
	If is_lucky is False, the diver misses the fish by invoking the miss method and return the relevant message:
"{diver_name} missed a good {fish_name}."
o	If the diver’s oxygen_level is greater than the fish's time_to_catch value, the fish is caught, and the diver hits with the harpoon. The method returns:
"{diver_name} hits a {points}pt. {fish_name}."
•	Zero Oxygen Level Handling:
o	If, at any point during the chase, the diver's oxygen_level drops to 0, the diver has_health_issue property is set to True.
health_recovery()
The method doesn't receive any parameters. Its main purpose is to scan through the collection of divers and identify those facing health issues:
Once the method identifies a diver with the has_health_issue property set to True, it initiates a series of actions to stabilize the diver:
•	First, it sets the has_health_issue property of the diver to False, indicating that the diver is now in a stable condition.
•	Secondly, it replenishes the diver's oxygen_level back to its maximum, ensuring the divers are ready for the next dive when they feel comfortable.
•	Returns the following message:
"Divers recovered: {count}"
diver_catch_report(diver_name: str)
Returns detailed information about a specific diver and his catch so far:
"**{diver_name} Catch Report**
{fish details1}
{fish details2}
…
{fish detailsn}"
competition_statistics()
Return information about each diver, arranging them in descending order based on competition_points. If more than one diver has the same number of points, further arrange them in descending order based on the count of catches. For divers with the same catch count, arrange them alphabetically by name. Return only divers that are in good health condition. To receive the correct output, use the __str__()method of each diver:
"**Nautical Catch Challenge Statistics**
{diver1}
{diver2}
"""
from project.nautical_catch_challenge_app import NauticalCatchChallengeApp


nautical_catch_challenge = NauticalCatchChallengeApp()

# Dive into competition
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

# Swim into competition
print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# Check health recovery
print(nautical_catch_challenge.health_recovery())

# Conduct fishing competitions
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))

# View catch reports
print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))

# View competition statistics
print(nautical_catch_challenge.competition_statistics())

"""
MaxineHarper is successfully registered for the competition as a ScubaDiver.
JamalCarter is successfully registered for the competition as a FreeDiver.
SkyDiver is not allowed in our competition.
OscarWallace is successfully registered for the competition as a FreeDiver.
LilaMoreno is successfully registered for the competition as a ScubaDiver.
LilaMoreno is already a participant.
ReefFish is forbidden for chasing in our competition.
BluestripeSnapper is allowed for chasing as a DeepSeaFish.
YellowtailSurgeonfish is allowed for chasing as a PredatoryFish.
Barracuda is allowed for chasing as a PredatoryFish.
Coryphaena is allowed for chasing as a PredatoryFish.
Bluefish is allowed for chasing as a PredatoryFish.
SwordFish is allowed for chasing as a DeepSeaFish.
Mahi-Mahi is allowed for chasing as a DeepSeaFish.
Tuna is allowed for chasing as a DeepSeaFish.
AquariumFish is forbidden for chasing in our competition.
Barracuda is already permitted.
FionaBennett is not registered for the competition.
The SilverArowana is not allowed to be caught in this competition.
MaxineHarper hits a 5.0pt. YellowtailSurgeonfish.
MaxineHarper hits a 9.1pt. Mahi-Mahi.
MaxineHarper hits a 8.5pt. Tuna.
MaxineHarper hits a 9.7pt. Coryphaena.
MaxineHarper will not be allowed to dive, due to health issues.
OscarWallace hits a 9.2pt. Barracuda.
OscarWallace missed a good YellowtailSurgeonfish.
OscarWallace will not be allowed to dive, due to health issues.
JamalCarter hits a 9.2pt. Barracuda.
JamalCarter missed a good YellowtailSurgeonfish.
LilaMoreno hits a 8.5pt. Tuna.
LilaMoreno hits a 9.1pt. Mahi-Mahi.
LilaMoreno hits a 10.0pt. SwordFish.
Divers recovered: 4
LilaMoreno hits a 8.5pt. Tuna.
LilaMoreno hits a 9.1pt. Mahi-Mahi.
LilaMoreno hits a 10.0pt. SwordFish.
**LilaMoreno Catch Report**
DeepSeaFish: Tuna [Points: 8.5, Time to Catch: 180 seconds]
DeepSeaFish: Mahi-Mahi [Points: 9.1, Time to Catch: 180 seconds]
DeepSeaFish: SwordFish [Points: 10.0, Time to Catch: 180 seconds]
DeepSeaFish: Tuna [Points: 8.5, Time to Catch: 180 seconds]
DeepSeaFish: Mahi-Mahi [Points: 9.1, Time to Catch: 180 seconds]
DeepSeaFish: SwordFish [Points: 10.0, Time to Catch: 180 seconds]
**Nautical Catch Challenge Statistics**
ScubaDiver: [Name: MaxineHarper, Oxygen level left: 540, Fish caught: 4, Points earned: 32.3]
FreeDiver: [Name: JamalCarter, Oxygen level left: 120, Fish caught: 1, Points earned: 9.2]
FreeDiver: [Name: OscarWallace, Oxygen level left: 120, Fish caught: 1, Points earned: 9.2]
"""