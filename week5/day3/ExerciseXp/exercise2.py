from locale import currency


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}'

    def __int__(self):
        return self.amount

    def __repr__(self):
      return f"{self.amount} {self.currency} "

    def __add__(self, other):
        if (isinstance(other,Currency) and self.currency == other.currency):
            return self.amount + other.amount
        elif (isinstance(other,int)):    
            return self.amount + other   
        else:
            raise Exception ("Currency Mismatch")
        
    def __iadd__(self, other):
        self.amount = self.__add__(other)
        return self
    
           

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)




print(str(c4))
print(int(c3))
print(c1 + 5)
print(c1+c2)
print(c1)
c1+=90
print(c1)

#print(c1+c3)