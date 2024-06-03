from unittest import TestCase, main

from project.shopping_cart import ShoppingCart

class TestShoppingCart(TestCase):

    def setUp(self):
        self.shoppingcart = ShoppingCart('Terra', 20)

    def test_init(self):
        self.assertEqual('Terra', self.shoppingcart.shop_name)
        self.assertEqual(20, self.shoppingcart.budget)
        self.assertEqual({}, self.shoppingcart.products)

    def test_raise_valueerror_without_start_uppercase(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.shop_name = 'terra'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))


    def test_raise_valueerror_with_contain_dijits(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.shop_name = 'T3rra'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_raise_valueerror_because_of_expensive_product(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.add_to_cart('sox', 100.00)

        self.assertEqual("Product sox cost too much!", str(ve.exception))

    def test_add_product_with_succsses(self):
        self.assertEqual('sox product was successfully added to the cart!', self.shoppingcart.add_to_cart('sox', 99.99))
        self.assertEqual({'sox': 99.99}, self.shoppingcart.products)

    def test_raise_valueerror_if_product_for_remove_not_in_cart(self):
        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.remove_from_cart('hat')

        self.assertEqual('No product with name hat in the cart!', str(ve.exception))

    def test_remove_product_with_succsses(self):
        self.shoppingcart.add_to_cart('sox', 99.99)
        self.assertEqual("Product sox was successfully removed from the cart!", self.shoppingcart.remove_from_cart('sox'))
        self.assertEqual({}, self.shoppingcart.products)

    def test_add_new_cart(self):
        self.shoppingcart.add_to_cart('from Terra', 2)
        other = ShoppingCart('Lc', 150)
        other.add_to_cart("from Lc", 1)

        merge = self.shoppingcart.__add__(other)

        self.assertEqual('TerraLc', merge.shop_name)
        self.assertEqual(170, merge.budget)
        self.assertEqual({'from Terra': 2, 'from Lc': 1}, merge.products)

    def test_buy_products_raise_valueerrror_low_budget(self):
        self.shoppingcart.add_to_cart('from Terra', 22)

        with self.assertRaises(ValueError) as ve:
            self.shoppingcart.buy_products()

        self.assertEqual(f"Not enough money to buy the products! Over budget with 2.00lv!", str(ve.exception))


    def test_buy_products_with_succssess(self):
        self.shoppingcart.add_to_cart('from Terra', 15)

        self.assertEqual(f"Products were successfully bought! Total cost: 15.00lv.", self.shoppingcart.buy_products())




if __name__ == "__main__":
    main()

