#Exercise 1 : Hello World-I Love Python
print("Hello World\n" * 4 + "I Love Python\n" * 4)

#Exercise 2 : What Is The Season ?
#Ask the user to input a month (1 to 12)
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)
user_in = int(input("Please enter a month: "))
if (user_in >= 3 and user_in <= 5):
    print("Spring runs from March to May")
elif (user_in >= 6 and user_in <= 8):
    print("Summer runs from June to August")
elif (user_in >= 9 and user_in <= 11):
    print("Autumn runs from September to November")
elif (user_in >= 12 and user_in <= 2):
    print("Winter runs from December to February")
else:
    print("Selection should be between 1 to 12, invalid entry. Bye")
print("\n")
print("End of ExerciseXpGold")