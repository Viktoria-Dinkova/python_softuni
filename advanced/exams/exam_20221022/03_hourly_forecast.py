"""
Write a function called forecast that stores information about the weather, and returns sorted information for all locations. The function will receive a different number of arguments.
The arguments will be passed as tuples with two elements - the first one is the location, and the second one is the weather:
•	Location name: string
o	any string
•	Weather: string
o	"Sunny"
o	"Rainy"
o	"Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations with cloudy weather, and last are the locations with rainy weather.
 For each sequence of locations (e.g. all sunny locations), sort them by their name in ascending order (alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function
Output
•	The output should look like this:
"{first_sorted_location} - {weather}"
"{second_sorted_location} - {weather}"
…
"{last_sorted_location} - {weather}"

"""


def forecast(*weather_data):

    result = ''

    data = {"Sunny": [],
            "Cloudy": [],
            "Rainy": []
            }

    for loc in weather_data:
        town, weather = loc
        if weather == "Sunny":
            data['Sunny'].append(town)
        elif weather == "Cloudy":
            data["Cloudy"].append(town)
        elif weather == "Rainy":
            data["Rainy"].append(town)

    for k, v in data.items():
        if len(v) > 0:
            for t in sorted(v):
                result += f'{t} - {k}\n'

    return result
#
# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
