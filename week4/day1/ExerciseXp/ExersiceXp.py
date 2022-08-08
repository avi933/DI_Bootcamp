#Exercise 1 : Hello World
print("hello world \n" * 4)

#Exercise 2 : Some Math
base = 99
power = 3
rest = pow(base, 3)
print(rest, "\n")
final_result = (rest * 8)
print(final_result, "\n")

#Exercise 3 : What Is The Output ?
print(5 < 3)  #False
print(3 == 3)  #True
print(3 == "3")  #False
#print("3" > 3) #Error
print("Hello" == "hello", "\n")  #False

#Exercise 4 : Your Computer Brand
computer_brand = "Dell"
print("I have a " + computer_brand + " computer", "\n")

#Exercise 5 : Your Information
name = "Avishek"
age = "29"
shoe_size = "41"
info = "my name is " + name + ". I'm " + age + " and my shoe size is " + shoe_size
print(info, "\n")

# Exercise 6 : A & B
a = 30
b = 20

if a > b:
    print("Hello world\n")
print("Next Exercise\n")

#Exercise 7 : Odd Or Even
#Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input("Please enter a number "))

if (num % 2) == 0:
    print(str(num) + " is an even number")
else:
    print(str(num) + " is an Odd number")
print("Next Exercise\n")

#Exercise 8 : What’s Your Name ?
#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

fname = input("Please enter your name:")
cname = "Avishek"
if fname == cname:
    print("Hey we have the same name bro")
else:
    print("Sorry bro we have different name")
print("Next Exercise\n")

#Exercise 9 : Tall Enough To Ride A Roller Coaster
height = int(input("please enter your name in inches: "))
height_in_cm = height * 2.54
if height_in_cm >= 145:
    print("Tall enough to ride\n")
else:
    print("Need to grow some more to ride\n")

print("End of exercise Xp")
