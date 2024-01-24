# Create a class Catalogue. The __init__ method should accept the name of the catalogue (string).
# Each catalogue should also have an attribute called products, an empty list.
# The class should also have three more methods:
# •	add_product(product_name: str) - adds the product to the products' list
# •	get_by_letter(first_letter: str) - returns a list containing only the products that start with the given letter
# •	__repr__ - returns the catalogue info in the following format:
# "Items in the {name} catalogue:
# {item1}
# {item2}
# …
# {itemN}"
# The items should be sorted alphabetically in ascending order.

class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        filtred_products = [x for x in self.products if x[:1] == first_letter]
        return filtred_products

    def __repr__(self):
        catalogue_products = sorted(self.products)
        catalogue_products = "\n".join(catalogue_products)
        catalogue_info = f'Items in the {self.name} catalogue:\n{catalogue_products}'
        return catalogue_info

'''
catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
'''