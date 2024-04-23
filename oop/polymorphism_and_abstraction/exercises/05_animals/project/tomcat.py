from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Male")


    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"


    def make_sound(self):
        return "Hiss"
