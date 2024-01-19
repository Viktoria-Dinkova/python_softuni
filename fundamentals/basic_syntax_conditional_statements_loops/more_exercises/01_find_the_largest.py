# You will be given a number. Print the largest number that can be formed from the digits of the given number.
# You will be given a number. Print the largest number
# that can be formed from the digits of the given number.

numbers = input()
nines, eights, sevens, sixes, fives, fours, threes, twos, ones, zeros = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for num in numbers:
    int_num = int(num)

    if int_num == 9:
        nines += 1

    elif int_num == 8:
        eights += 1

    elif int_num == 7:
        sevens += 1

    elif int_num == 6:
        sixes += 1

    elif int_num == 5:
        fives += 1

    elif int_num == 4:
        fours += 1

    elif int_num == 3:
        threes += 1

    elif int_num == 2:
        twos += 1

    elif int_num == 1:
        ones += 1

    elif int_num == 0:
        zeros += 1

print(f'{"9" * nines}{"8" * eights}{"7" * sevens}{"6" * sixes}{"5" * fives}{"4" * fours}{"3" * threes}{"2" * twos}{"1" * ones}{"0" * zeros}')



