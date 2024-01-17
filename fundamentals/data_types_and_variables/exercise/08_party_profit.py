# You will receive a group size. After that, you receive the days of the adventure.
# Every day, you earn 50 coins, but you also spend 2 coins per companion for food.
# Every 3rd (third) day, you organize a motivational party, spending 3 coins per companion for drinking water.
# Every 5th (fifth) day, you slay a boss monster and gain 20 coins per companion. But if you have a motivational party the same day, you spend additional 2 coins per companion.
# Every 10th (tenth) day at the start of the day, 2 (two) of your companions leave, but every 15th (fifteenth) day 5 (five) new companions are joined at the beginning of the day.
# You should calculate how many coins gets each companion at the end of the adventure.
# Input / Constraints
# The input will consist of exactly 2 lines:
# •	group size – integer in the range [1…100]
# •	days – integer in the range [1…100]
# Output
# Print the following message: "{companions_count} companions received {coins} coins each."
# Note: You cannot split a coin, so you should round down the coins to an integer number.

group_size = int(input())
adventures_days = int(input())

earn_coins_per_day = 50
spend_coins_per_companion = 2
earn_coins = 0

for day in range(1,adventures_days + 1):
    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    earn_coins += earn_coins_per_day
    earn_coins -= spend_coins_per_companion * group_size

    if day % 3 == 0:
        earn_coins -= 3 * group_size

    if day % 5 == 0:
        earn_coins += 20 * group_size
        if day % 3 == 0:
            earn_coins -= 5 * group_size

print(f'{group_size} companions received {earn_coins} coins each.')


