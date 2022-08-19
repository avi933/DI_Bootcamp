class Cat:
    def __init__(self, cat_name,age):
        self.name = cat_name
        self.age = age
        print("Cat name is ", cat_name, " and age is ",age)        
cat1 = Cat("Billy",2)
cat2 = Cat("Milly",3)
cat3 = Cat("Polly",5)
cats = [cat1,cat2,cat3]

def older(cats):
  oldest = cat1
  for i in range(len(cats)):
    if (cats[i].age > oldest.age):
       oldest = cats[i]
    
  print(f"{cats[i].name} is {cats[i].age} years old and is the oldest")

older(cats)



