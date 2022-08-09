#Exercise 1 : Set
#Create a set called my_fav_numbers with all your favorites numbers.
my_fav_numbers = [2, 4, 8, 20]
print("my fav numbers are: " + str(my_fav_numbers), "\n")

#Add two new numbers to the set.
my_fav_numbers.append(25)
my_fav_numbers.append(30)
print("New list of fav num is: " + str(my_fav_numbers), "\n")

#Remove the last number
my_fav_numbers.remove(my_fav_numbers[-1])
print("list after removing last number: " + str(my_fav_numbers), "\n")

#Create a set called friend_fav_numbers
friend_fav_numbers = [3, 5, 20, 69]

#Concatenate my_fav_numbers and friend_fav_numbers
our_fav_numbers = my_fav_numbers + friend_fav_numbers
print("After adding both list: " + str(our_fav_numbers), "\n")