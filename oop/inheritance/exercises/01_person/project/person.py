"""
You are asked to model an application for storing data about people. You should be able to have a Person and a Child.
Every person receives username and age upon initialization. Your task is to model the application.
Create a Child class that inherits a Person and has the same constructor definition. However, do not copy the code from the Person class - reuse the Person class's constructor.
Submit in judge a zip file named project, containing a separate file (person.py and child.py) for each of the classes.
"""

class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age