"""
In the registration.py, create a class called Registration. Upon initialization, It will not receive anything, but we'll have these three methods.
-	add_user(user: User, library: Library):
o	Adds the user if we do not have them in the library's user records already
o	Otherwise, returns the message "User with id = {user_id} already registered in the library!"
-	remove_user(user: User, library: Library):
o	Removes the user from the library records if present
o	Otherwise, returns the message "We could not find such user to remove!"
-	change_username(user_id: int, new_username: str, library: Library):
o	If there is a record with the same user id in the library and the username is different than the provided one, change the username with the new one provided and return the message "Username successfully changed to: {new_username} for user id: {user_id}". Changes his username in the rented_books dictionary as well (if present).
o	If the new username is the same for this id, return the following message "Please check again the provided username - it should be different than the username used so far!".
o	If there is no record for the provided id return "There is no user with id = {user_id}!"
"""
from project.library import Library
from project.user import User


class Registration:

    def add_user(self, user: User, library: Library) -> str:
        if user not in library.user_records:
            library.user_records.append(user)

        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)

        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        try:
            curr_user = next(filter(lambda lu: lu.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if curr_user.username != new_username:
            curr_user.username = new_username

            try:
                library.rented_books[new_username] = library.rented_books.pop(curr_user.username)
            except KeyError:
                pass

            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return f"Please check again the provided username - it should be different than the username used so far!"

