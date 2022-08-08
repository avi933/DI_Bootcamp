#Exercise3

3 <= 3 < 9  #True
3 == 3 == 3  #True
bool(0)  #False
bool(5 == "5")  #False
bool(4 == 4) == bool("4" == "4")  #False
bool(bool(None))  #False
x = (1 == True)  #True
y = (1 == False)  #False
a = True + 4
b = False + 10

print("x is", x)  #value of x is True
print("y is", y)  #value of y is False
print("a:", a)  # value of a is 5
print("b:", b)  #value of b is 10

#Exercise 4 : How Many Characters In A Sentence ?
my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
print("There are " + str(len(my_text)) + " in the sentence\n")

print("Next Exercise")
#Exercise 5: Longest Word Without A Specific Character
longest = input("Enter the longest word without letter A:\n")
if "a" in longest:
    print("Sorry the word contain A")
else:
    print("Congratulation")
print("End of ExerciseXpNinja")
