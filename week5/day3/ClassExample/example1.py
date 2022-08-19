from mimetypes import init


class Dog:
    no_of_dog = 0 
    def __init__(self,name,age,weight):
        self.name = name
        self.__age = age
        self.weight = weight
        Dog.no_of_dog =+ 1
        print(f'a new dog is {self.name}')

    def running_speed(self):
        return self.weight / self.age * 10

    @property
    def age(self):
        return self.__age 
    def set_age(self,age):
        if age > 30:
            pass
        else:
         self.__age = age 

    

avi_dog = Dog("Rolly",5,25)
Nayar_dog = Dog("Olly",6,15)

print(Dog.no_of_dog)

print(f'avi dog age is {avi_dog.age}')

avi_dog.set_age(100) ## will return initial age,due to condition in set age
avi_dog.set_age(20)

print(f'avi dog age is {avi_dog.age}')
#print(f'{avi_dog.running_speed()}')