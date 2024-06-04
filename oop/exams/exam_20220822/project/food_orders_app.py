from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_MEALS = {"Starter": Starter,
                   "MainDish": MainDish,
                   "Dessert": Dessert
                   }
    RECEIPT_ID = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str) -> str:
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if client:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal) -> None:
        for meal in meals:
            if meal.__class__.__name__ not in self.VALID_MEALS:
                pass

            new_meal = self.VALID_MEALS[meal.__class__.__name__](meal.name, meal.price, meal.quantity)
            self.menu.append(new_meal)

    def show_menu(self) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities: (str, int)) -> str:
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        for meal in meal_names_and_quantities:
            menu_meal = [m for m in self.menu if m.name == meal]

            if not menu_meal:
                raise Exception(f"{meal} is not on the menu!")

            menu_meal_for_order = menu_meal[0]
            if menu_meal_for_order.quantity < meal_names_and_quantities[meal]:
                raise Exception(f"Not enough quantity of {menu_meal_for_order.__class__.__name__}: {meal}!")

            meal_for_order = menu_meal_for_order.__class__(meal, menu_meal_for_order.price, meal_names_and_quantities[meal])
            client[0].shopping_cart.append(meal_for_order)
            client[0].bill += meal_for_order.price * meal_for_order.quantity
            menu_meal_for_order.quantity -= meal_for_order.quantity

            client_orders = []
            order_price = 0.00
            for co in client[0].shopping_cart:
                client_orders.append(co.name)
                order_price += co.price * co.quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(client_orders)} for {order_price:.2f}lv."

    def cancel_order(self, client_phone_number: str) -> str:
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if not client[0].shopping_cart:
            raise Exception("There are no ordered meals!")

        for co in client[0].shopping_cart:
            co_in_menu = [mo for mo in self.menu if co.name == mo.name]
            co_in_menu[0].quantity += co.quantity

        client[0].shopping_cart.clear()
        client[0].bill = 0.0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str) -> str:
        total_paid_money = 0
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]
        if not client[0].shopping_cart:
            raise Exception("There are no ordered meals!")

        for co in client[0].shopping_cart:
            total_paid_money += co.price * co.quantity

        self.RECEIPT_ID += 1
        client[0].shopping_cart.clear()
        client[0].bill = 0.0

        return f"Receipt #{self.RECEIPT_ID} with total amount of {total_paid_money:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
