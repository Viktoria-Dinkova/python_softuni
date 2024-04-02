"""
Create a class called Account. Upon initialization, it should receive an id, a balance, and a pin (all numbers). The pin and the id should be private instance attributes, and the balance should be a public attribute. Create two public instance methods:
•	get_id(pin) - if the given pin is correct, return the id, otherwise, return "Wrong pin"
•	change_pin(old_pin, new_pin) - if the old pin is correct, change it to the new one and return "Pin changed", otherwise return "Wrong pin"
"""

class Account:
    WRONG_PIN = "Wrong pin"

    def __init__(self, id: int, balance: int, pin: int):
        self.__id = id
        self.balance = balance
        self.__pin = pin


    def get_id(self, pin) -> int or str:
        if pin == self.__pin:
            return self.__id
        return Account.WRONG_PIN

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if self.get_id(old_pin) == self.__id:
            self.__pin = new_pin
            return "Pin changed"
        return Account.WRONG_PIN

