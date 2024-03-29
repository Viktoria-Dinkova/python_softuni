# Create a class Vehicle. The __init__ method should receive a type, a model, and a price.
# You should also set an owner to None. The class should have the following methods:
# •	buy(money: int, owner: str)
# o	If the person has enough money and the vehicle has no owner, returns: "Successfully bought a {type}. Change: {change}" and sets the owner to the given one
# o	If the money is not enough, return: "Sorry, not enough money"
# o	If the car already has an owner, return: "Car already sold"
# •	sell()
# o	If the car has an owner, set it to None again.
# o	Otherwise, return: "Vehicle has no owner"
# •	__repr__()
# o	If the vehicle has an owner, returns: "{model} {type} is owned by: {owner}".
# o	Otherwise, return: "{model} {type} is on sale: {price}"

class Vehicle:
    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money: int, owner: str) -> str:
        message = ''
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price
            message += f'Successfully bought a {self.type}. Change: {change:.2f}'
        elif money < self.price:
            message += 'Sorry, not enough money'
        elif self.owner is not None:
            message += 'Car already sold'

        return message

    def sell(self) -> str:
        if self.owner is not None:
            self.owner = None
        else:
            return 'Vehicle has no owner'

    def __repr__(self):
        message = ''
        if self.owner is None:
            message += f'{self.model} {self.type} is on sale: {self.price}'
        else:
            message += f'{self.model} {self.type} is owned by: {self.owner}'

        return message

'''
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
'''