# Да се напише конзолна програма, която прочита възраст (реално число) и пол ('m' или 'f'), въведени от потребителя,
# и отпечатва обръщение измежду следните:
# •	"Mr." – мъж (пол 'm') на 16 или повече години
# •	"Master" – момче (пол 'm') под 16 години
# •	"Ms." – жена (пол 'f') на 16 или повече години
# •	"Miss" – момиче (пол 'f') под 16 години


age = float(input())
sex = input()
message = ''

if sex == 'f':
    if age >= 16:
        message = 'Ms.'
    else:
        message = 'Miss'
elif sex == 'm':
    if age >= 16:
        message = 'Mr.'
    else:
        message = 'Master'

print(f'{message}')
