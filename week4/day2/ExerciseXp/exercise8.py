#Exercise 8: Who Ordered A Pizza ?
#Write a loop that asks a user to enter topping
#the user inputs ‘quit’ stop asking
topping_list = []
active = True
while active:
    topping = input(
        "Please enter the name of a topping you wish to have (enter 'quit' when you are finished): "
    )
    if topping == 'quit':
        active = False
    else:
        topping_list.append(topping)
print(topping_list)
total = (10 + (2.5 * len(topping_list)))
print("the total price of the piza with the toppings is " + str(total))
