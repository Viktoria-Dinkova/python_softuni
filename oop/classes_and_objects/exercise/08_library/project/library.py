"""
In the library.py create a class Library. Upon initialization, it will not receive anything, but it should have the following instance attributes:
o	user_records - an empty list that will store the users (users objects) of the library
o	books_available - an empty dictionary that will keep information regarding the authors (key: str) and the books available for each of the authors (list of strings)
o	rented_books - an empty dictionary that will keep information regarding the usernames (key: str) and nested dictionary as a value which will keep information regarding the book names (key: str) and days left before returning the book to the library (int) - ({usernames: {book names: days to return}}).
You should also create 2 additional instance methods:
-	get_book(author: str, book_name: str, days_to_return: int, user: User):
o	If the book is available in the library add it to the books list for this user, update the library records (rented_books and available_books dicts), and return the following message: "{book_name} successfully rented for the next {days_to_return} days!"
o	If it is already rented, return the following message "The book "{book_name}" is already rented and will be available in {days_to_return provided by the user rented the book} days!"
-	return_book(author:str, book_name:str, user: User):
o	If the book is in the user's books list, returns it to the library (update books_available and rented_books class attributes) and remove it from the books list for this user
o	Otherwise, returns the following message "{username} doesn't have this book in his/her records!"
"""
from typing import List, Dict
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available: Dict[str: List[str]] = {}
        self.rented_books: Dict[str: Dict[str: int]] = {} #{usernames: {book names: days to return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:

            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {book_name: days_to_return}
            else:
                self.rented_books[user.username][book_name] = days_to_return

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for curr_book in self.rented_books.values():
            if book_name in curr_book:
                left_days = curr_book[book_name]
            return f'The book "{book_name}" is already rented and will be available in {left_days} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]

        return f"{user.username} doesn't have this book in his/her records!"

