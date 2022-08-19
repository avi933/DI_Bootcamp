class Dog :
  def __init__(self,name,age,weight):
    self.name = name
    self.age = age
    self.weight = weight
  def bark(self):
    print(f'{self.name} is barking')
  
  def run_speed(self):
    speed = 0 
    speed = ((self.weight/self.age)*10)
    #print(f'{self.name} speed is {speed}')
    return (speed)
    
  def fight(self,other_dog):
    print(f'{self.name} is fighting')
    other_dog_speed = other_dog.run_speed() * other_dog.weight  
    dog1_speed = dog1.run_speed() * dog1.weight
     
    if dog1_speed > other_dog_speed:
     print(f'{dog1.name} is the winner and speed is {dog1_speed}' )
    else:
      print(f'{other_dog.name} is the winner')

  def addOperator(x,y):
    sum = x + y 
    return sum

   
    
dog1= Dog("Rex",4,30)
other_dog=Dog("Tommy",2,40)
print(f'first dog name is {dog1.name}')
print(f'second dog name is {other_dog.name}')
dog1.bark()
dog1.run_speed()

other_dog.fight(dog1)

