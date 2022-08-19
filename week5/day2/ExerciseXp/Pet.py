# Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return (f'{self.name} is just walking around')

class Bengal(Cat):
    def sing(self, sounds):
        return (f'{sounds}')

class Chartreux(Cat):
    def sing(self, sounds):
        return (f'{sounds}')

class Siamese(Cat):
  pass

Bengal_1=Bengal("milly",3)
Chartreux_1 = Chartreux("polly",2)
Siamese_1 = Siamese("rolly",4)

all_cats = [Bengal_1,Chartreux_1,Siamese_1 ]
sara_pets = all_cats
pet1 = Pets(all_cats)
pet1.walk()
  