
try:
    age = int(input('Enter Your age '))
    print(age)
except ValueError:
    print('invalid data' )

user = [
    {"name":"selim", "age": 30},
    {"name": "sammy", "age": 20},
]

print((user))