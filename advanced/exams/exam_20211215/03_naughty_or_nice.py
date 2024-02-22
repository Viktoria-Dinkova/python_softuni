"""
Write a function called naughty_or_nice_list which will receive
•	A list representing Santa Claus' "Naughty or Nice" list full of kids' names
•	A different number of arguments (strings) and/or keywords representing commands
The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
The list holds a different number of kids - tuples containing two elements: a counting number (integer) at the first position and a name (string) at the second position.
For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
Next, the function could receive arguments and/or keywords.
Each argument is a command. The commands could be the following:
•	"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to a list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.
•	"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
•	If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids depending on the value in the keyword. Then, remove it from the Santa list.
•	Otherwise, ignore the command.
All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
In the end, return the final lists, each on a new line as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
Output
•	The function should return strings with the names on each list on separate lines, if there are any, otherwise skip the line:
o	"Nice: {name1}, {name2} … {nameN}"
o	"Naughty: {name1}, {name2} … {nameN}"
o	"Not found: {name1}, {name2} … {nameN}"

"""
def naughty_or_nice_list(santa, *children, **kwargs):
    end_list = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    result = ''
    for_del = []

    for kid in children:
        val, type = kid.split('-')
        santa_count = 0
        for s in santa:
            if s[0] == int(val):
                santa_count += 1

        if santa_count == 1:
            for ss in santa:
                if ss[0] == int(val):
                    end_list[type].append(ss[1])
                    for_del = (ss[0], ss[1])
                    break
            santa.remove(for_del)

    for kid_name, kid_type in kwargs.items():
        santa_count = 0
        for s in santa:
            if s[1] == kid_name:
                santa_count += 1

        if santa_count == 1:
            for ss in santa:
                if ss[1] == kid_name:
                    end_list[kid_type].append(ss[1])
                    for_del = (ss[0], ss[1])
                    break
            santa.remove(for_del)

    for se in santa:
        end_list["Not found"].append(se[1])

    for i, j in end_list.items():
        if j:
            result += f'{i}: {", ".join(j)}\n'

    return result



