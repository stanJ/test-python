class Animal(object):
    pass
# 大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print('running...')
class Flyable(object):
    def fly(self):
        print('flying...Animal')
#各种动物
class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Flyable):
    pass
class Parrot(Bird, Flyable):
    pass
class Ostrich(Bird, Runnable):
    pass



dog = Dog()
dog.run()
os = Ostrich()
os.run()