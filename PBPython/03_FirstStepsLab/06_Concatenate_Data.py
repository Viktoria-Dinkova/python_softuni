'''
Напишете програма, която прочита от конзолата име, фамилия, възраст и град
и печата следното съобщение: "You are <firstName> <lastName>, a <age>-years old person from <town>."
'''

firstName = input()
lastName = input()
age = input()
town = input()

greeting = f'You are {firstName} {lastName}, a {age}-years old person from {town}.'

print(greeting)
