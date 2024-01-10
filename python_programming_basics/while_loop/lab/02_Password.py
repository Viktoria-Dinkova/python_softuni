# Напишете програма, която първоначално прочита име и парола на потребителски профил. След това чете парола за вход.
# •	при въвеждане на грешна парола: потребителя да се подкани да въведе нова парола.
# •	при въвеждане на правилна парола: отпечатваме "Welcome {username}!".

u_name = input()
u_pass = input()

curr_pass = ''

while curr_pass != u_pass:
    curr_pass = input()
    if curr_pass == u_pass:
        print(f'Welcome {u_name}!')
        break

