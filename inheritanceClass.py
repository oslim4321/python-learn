# class Dog:
#     def walk(self):
#         print('walk')
#
# class Cat:
#     def walk(self):
#         print('walk')
#
#


class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def beAnnoying(self):
       print('annoying')


dog1 = Dog()
cat1 = Dog()

dog1.walk()
dog1.bark()

cat1.walk()
cat1.bark()


