def say_hello():
    
    print("Hello!") 

say_hello()

def is_even(num):
    if num%2 ==0 :
        return True,f"{num} is even"
    else:
        return False,f"{num} is odd"
x = is_even(2)
print(x[1])
print(is_even(5))