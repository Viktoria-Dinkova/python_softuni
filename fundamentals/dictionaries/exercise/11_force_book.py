# The force users struggle to remember which side is the different force users from because they switch them too often.
# So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
# •	If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# •	Only if there is no such force user in any force side -> add the force user to the corresponding side.
# •	If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# •	If there is such force user already -> change their side.
# •	If there is no such force user in any force side -> add the force user to the corresponding force side.
# •	If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# •	Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. For each side, print the force users.
# In case there are no force users on a side, you shouldn't print the side information.
force_book = {}
sides = []
users = []
while True:

    # function to return key for any value
    def get_key(val, my_dict):
        for key, value in my_dict.items():
            if val in value:
                return key
    def income(side: str, user: str):
        if (side not in sides) and (user not in users):
            force_book[side] = [user]
        elif user not in users:
            force_book[side].append(user)

        sides.append(side)
        users.append(user)

    def change(side: str, user: str):
        if user in users:
            old_side = get_key(user, force_book)
            force_book[old_side].remove(user)
            force_book[side].append(user)
        elif (side not in sides) and (user not in users):
            force_book[side] = [user]
        else:
            force_book[side].append(user)

        sides.append(side)
        users.append(user)
        print(f'{user} joins the {side} side!')

    in_lines = input()
    if in_lines == 'Lumpawaroo':
        for k,v in force_book.items():
            print(f'Side: {k}, Members: {len(v)}')
            for hero in v:
                print(f'! {hero}')
        break

    elif ' | ' in in_lines:
        hero = in_lines.split(' | ')
        income(hero[0], hero[1])
    elif ' -> ':
        hero = in_lines.split(' -> ')
        change(hero[1], hero[0])


