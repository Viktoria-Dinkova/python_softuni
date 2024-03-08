"""
Write a function called "cookbook" to assist Alex in arranging his recipes systematically.
The function will receive a variable number of arguments, passed as tuples containing three elements:
    the first element is the recipe's name,
    the second is the cuisine, and the third is a list of ingredients e.g., ("Recipe Name", "Cuisine", ["Ingredient 1", "Ingredient 2"]).
The objective is to sort the recipes by their cuisine, arranging Alex's collection based on the number of recipes in each cuisine in descending order.
In cases where two or more cuisines have the same number of recipes, they should be returned in ascending order (alphabetically) by cuisine.
Within each cuisine group, the recipes should be sorted in ascending order (alphabetically) by the recipe's name.
To aid Alex in quickly assessing the number of recipes in each cuisine group, the function should print the count of recipes next to each cuisine.
Furthermore, for each recipe within a cuisine group, display the necessary ingredients.
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function
Output
•	The output should look like this (before the star, there are two empty spaces.):
"{cuisine_1} cuisine contains {number_of_recipes_in_the_cuisine_group} recipes:
  * {recipe_name_1} -> Ingredients: {ingredient_1}, {ingredient_2}, ...
  * {recipe_name_2} -> Ingredients: {ingredient_1}, {ingredient_2}, ...
  ...
  * {recipe_name_n} -> Ingredients: {ingredient_1}, {ingredient_2}, ...
{cuisine_2} cuisine contains {number_of_recipes_in_the_cuisine_group} recipes:
  * {recipe_name_1} -> Ingredients: {ingredient_1}, {ingredient_2}, ...
  ...
  * {recipe_name_n} -> Ingredients: {ingredient_1}, {ingredient_2}, ... {cuisine_n} cuisine contains {number_of_recipes_in_the_cuisine_group} recipes:
  * {recipe_name_1} -> Ingredients: {ingredient_1}, {ingredient_2}, ..."
"""


def cookbook(*info):
    nationality = {}
    recipe = {}
    result = ''

    for data in info:
        name, cuisine, ingredients = data[0], data[1], data[2]

        if cuisine not in nationality:
            nationality[cuisine] = [name]
        else:
            nationality[cuisine].append(name)

        recipe[name] = ingredients

    for nk, nv in sorted(nationality.items(), key=lambda item: (-len(item[1]), item[0])):
        result += f"{nk} cuisine contains {len(nv)} recipes:\n"

        for rk, rv in sorted(recipe.items(), key=lambda item: item[0]):
            for j in nv:
                if j == rk:
                    result += f"  * {rk} -> Ingredients: {', '.join(rv)}\n"

    return result




print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
