list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1[3]) #displaying 4th item
list1[3] = 200 #changing the value in the array
print(list1) #printing new list with changed value

print("Next Exercise\n")

#exercise tuple
a_tuple = (10, 20, 30, 40) #creating a tuple
a, b, c, d = a_tuple #assigning it to variable
print(a) #displaying each item
print(b)
print(c)
print(d,"\n")

print("Next Exercise:")

#ask user for input and find its multiple
numbers = range(1, 13)
user_num = int(input("please enter a number: "))

for number in numbers:
  print(f"{number} x {user_num} = {number* user_num}")
print("\n")
print("Next Exercise:")

#printing number 1 to 10 using while loop 
counter = 1 
while counter <= 10:    
    print(counter)   
    counter += 1