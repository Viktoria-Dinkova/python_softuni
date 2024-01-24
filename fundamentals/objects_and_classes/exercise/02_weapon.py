# Create a class Weapon. The __init__ method should receive a number of bullets (integer).
# Create an attribute called bullets to store that number. The class should also have the following methods:
# •	shoot()
# o	If there are bullets in the weapon, reduce them by 1 and return a message "shooting..."
# o	If there are no bullets left, return: "no bullets left"
# •	__repr__()
# o	Returns "Remaining bullets: {amount_of_bullets}"
# o	You can read more about the method here: link

class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        info = ''

        if int(self.bullets) > 0:
            self.bullets -= 1
            info += 'shooting...'
        else:
            info += 'no bullets left'

        return info

    def __repr__(self):
        info = f'Remaining bullets: {self.bullets}'

        return info
'''
weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
'''