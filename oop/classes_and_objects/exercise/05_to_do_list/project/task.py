"""
The Task class should receive a username (string) and a due_date (str) upon initialization. A task also has two attributes: comments (empty list) and completed set to False by default.
The Task class should also have five additional methods:
-	change_name(new_name: str)
o	Changes the username of the task and returns the new username.
o	If the new username is the same as the current username, return "Name cannot be the same."
-	change_due_date(new_date: str)
o	Changes the due date of the task and returns the new date.
o	If the new date is the same as the current date, return "Date cannot be the same."
-	add_comment(comment: str)
o	Adds a comment to the task.
-	edit_comment(comment_number: int, new_comment: str)
o	The comment number value represents the index of the comment we want to edit. The method should change the comment and return all the comments, separated by comma and space (", ")
o	If the comment number is out of range, return "Cannot find comment."
-	details()
o	Returns the task's details in this format:
"Name: {task_name} - Due Date: {due_date}"
"""
from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name
        return self.name
    def change_due_date(self, new_date: str) -> str:
        if self.due_date == new_date:
            return "Date cannot be the same."

        self.due_date = new_date
        return self.due_date
    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str) -> str:
        if not (0 <= comment_number < len(self.comments)):
            return "Cannot find comment."

        self.comments[comment_number] = new_comment
        return f"{', '.join(self.comments)}"

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"
