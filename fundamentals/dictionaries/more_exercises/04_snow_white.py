# You will be receiving several input lines which contain data about each dwarf in the following format:
# {dwarf_name} <:> {dwarf_hat_color} <:> {dwarf_physics}
# The "dwarf_name" and the "dwarf_hat_color" are strings. The "dwarf_physics" is an integer.
# You must store the data about the dwarfs in your program. There are several rules though:
# •	If 2 dwarfs have the same name but different color, they should be considered different dwarfs, and you should store them both.
# •	If 2 dwarfs have the same name and the same color, store the one with the higher physics.
# When you receive the command "Once upon a time", the input ends. You must order the dwarfs by physics in descending order
# and then by total count of dwarfs with the same hat color in descending order.
# Then you must print them all.
dwarfs = {}
colors = {}
strenght = []
order = []
while True:
    info = input()
    if info == 'Once upon a time':
        break
    else:
        info = info.split(' <:> ')
        name = info[0]
        color = info[1]
        phisics = int(info[2])
        if name not in dwarfs:
            dwarfs[name] = {color: phisics}
            if color not in colors:
                colors[color] = 1
            else:
                colors[color] += 1
            order.append(name)

        elif (name in dwarfs) and (color not in dwarfs[name]):
            dwarfs[name][color] = phisics
            if color not in colors:
                colors[color] = 1
            else:
                colors[color] += 1

        elif (color in dwarfs[name]) and dwarfs[name][color] < phisics:
            dwarfs[name][color] = phisics

for x,y in dwarfs.items():
    for s,w in y.items():
        strenght.append(w)

ss_strenght = set(strenght)
set_strenght = sorted(ss_strenght, reverse=True)
colors = sorted(colors.items(), key=lambda v: v[1],reverse=True)

equal_color = [k[1] for k in colors]

if min(strenght) != max(strenght):

    for ss in set_strenght:
        for k,v in dwarfs.items():
            if ss in dwarfs[k].values():
                dwarf_color = [c for c, s in v.items()]
                print(f'({"".join(dwarf_color)}) {k} <-> {ss}')

elif min(colors) != max(colors):

    for more_color in colors:
        for k,v in dwarfs.items():
            if more_color[0] in dwarfs[k]:
                print(f'({more_color[0]}) {k} <-> {dwarfs[k][more_color[0]]}')

else:
    for p in order:
        for k, v in dwarfs.items():
            if k == p:
                for l,m in v.items():
                    print(f'({dwarfs[k][l]}) {k} <-> {dwarfs[k][l]}')



