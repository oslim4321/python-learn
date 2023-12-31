class Point:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def move(self):
        print('move')
    def draw(self):
        print('draw')

# point1 = Point('selim', '23')
# point1.x = 100
# point1.y = 200
#
# point1.draw()
# print(point1.y)

# constructor
# print(point1.name)
# print(point1.age)

# exercice
class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f'Hi i am {self.name}')


person1 = Person('sooto selim')
person2 = Person('sammy larry')

person1.talk()
person2.talk()
