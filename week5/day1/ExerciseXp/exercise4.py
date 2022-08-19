class Zoo():
  def __init__(self,zoo_name):
    self.animals=[]
    self.name = zoo_name
    
  def add_animal (self,new_animal):
    if new_animal not in self.animals:
      self.animals.append(new_animal)
      
  def get_animals(self):
    print(f"{self.animals}")
    
  def sell_animal(self,animal_sold):
    if animal_sold in self.animals:
      self.animals.remove(animal_sold)

  def sort_animals(self):
    self.animals.sort()
    print(f"{self.animals}")
  


the_zoo = Zoo("Avi")
the_zoo.get_animals()
the_zoo.add_animal("cat")
the_zoo.add_animal("snake")
the_zoo.add_animal("tigger")
the_zoo.get_animals()
the_zoo.sell_animal("snake")
the_zoo.get_animals()
the_zoo.add_animal('Emu')
the_zoo.add_animal('Cougar')
the_zoo.add_animal('Bear')
the_zoo.add_animal('Ape')
the_zoo.add_animal('Cat')
the_zoo.add_animal('Eel')
the_zoo.sort_animals()
