# A core idea of several left-wing ideologies is that the wealthiest should support the poorest, no matter what,
# and that is exactly what you are called to do for this problem.
# On the first line, you will be given the population (numbers separated by comma and space ", ").
# On the second line, you will be given the minimum wealth. You should distribute the wealth so that no part
# of the population has less than the minimum wealth. To do that, you should always take wealth from the wealthiest part of the population.
# There will be cases where the distribution will not be possible. In that case, print: "No equal distribution possible".

population = sorted([int(x) for x in input().split(', ')])
wealth = int(input())

low_list = [x for x in population if x < wealth]
high_list = [x for x in population if x >= wealth]

less_wealth = (wealth * len(low_list)) - sum(low_list)
more_wealth = sum(high_list) - (wealth * len(high_list))

if more_wealth < less_wealth:
    print(f'No equal distribution possible')
else:
    new_list = []
    high_list = high_list[::-1]
    head = []
    tie = []
    while len(low_list) > 0:
        miss_wealth = wealth - low_list[0]
        redundency = high_list[0] - wealth

        if redundency >= miss_wealth:
            head.append(wealth)
            low_list.pop(0)
            high_list = [high_list[0] - miss_wealth] + high_list[1:]
        else:
            tie.append(high_list[0])
            high_list.pop(0)

    tie += high_list
    tie = tie[::-1]
    new_list = head + tie

    print(new_list)


