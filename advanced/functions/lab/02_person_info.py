'''
Write a function called get_info that receives a name, an age, and a town and returns a string in the format:
"This is {name} from {town} and he is {age} years old". Use dictionary unpacking when testing your function.
Submit only the function in the judge system.
'''
def get_info(**kwargs):
    for k, v in kwargs.items():
        return (f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old")