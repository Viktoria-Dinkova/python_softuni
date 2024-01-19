# You will receive 2 lines of input. On the first line, you will receive a single string of integers, separated by a
# comma and a space ", ". On the second line, you will receive a count of beggars. Your job is to print a list with
# the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last number in
# the list. For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5],
# the second one collects [2, 4]. The same list with 3 beggars would produce a better outcome for the second
# beggar: 5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3]. Also, note that not all beggars have to
# take the same amount of "offers", meaning that the length of the list is not necessarily a multiple of n. The list
# length could be even shorter - i.e., the last beggars will take nothing (0).

offers = input().split(', ')
beggars_count = int(input())

collected_money = []

offers_as_num = []
for curr_offer in offers:
    offers_as_num.append(int(curr_offer))

for beggars in range(beggars_count):
    current_beggar_sum = 0

    for current_offer in range(beggars, len(offers_as_num), beggars_count):
        current_beggar_sum += offers_as_num[current_offer]

    collected_money.append(current_beggar_sum)

print(f'{collected_money}')
