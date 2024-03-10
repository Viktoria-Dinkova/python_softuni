"""
Create a class called Book. It should have an __init__() method that should receive:
•	username: string
•	author: string
•	pages: int
Submit only the class in the judge system.

"""


class Book:

    def __init__(self, name: str, author: str, pages: int):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Me", 200)
print(book.name)
print(book.author)
print(book.pages)
