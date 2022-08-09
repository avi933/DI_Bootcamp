#Exercise 5: For Loop
#Use a for loop to print all numbers from 1 to 20, inclusive.
print("printing number from 1 to 20")
numbers = range(1, 21)

for number in numbers:
    print(number)
print("\n")
#Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
print("Printing only even index")
numbers = range(1, 21, 2)

for number in numbers:
    print(number)
print("\n")