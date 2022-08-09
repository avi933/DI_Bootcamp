#Exercise 7: Favorite Fruits
fruits = input(
    "Enter your fav fruits, leave a blank space after each fruits: ")
fruit_list = fruits.split()
print(fruit_list)
found = False
fav_input = input("Enter one of your fav fruit\n")
# for fav in fruit_list:
#     print(fav, fav_input)
#     if fav_input == fav:
#         found = True
#         break

# if found == True:
#     print("You chose one of your fav fruit")
# else:
#     print("You chose a new fruit. I hope you enjoy\n")
if fav_input in fruit_list:
    print("you have chose your fav fruits")
else:
    print("You chose a new fruit. I hope you enjoy\n")