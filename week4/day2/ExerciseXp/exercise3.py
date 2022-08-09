#Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
#Remove “Banana” from the list.
basket.remove("Banana")
print("new list is :" + str(basket), "\n")
#Remove “Blueberries” from the list
basket.remove(basket[-1])
print("after removing blueberries " + str(basket), "\n")
#Add “Kiwi” to the end of the list
basket.append("kiwi")
#Add “Apples” to the beginning of the list
basket.insert(0, 'Apples')
print("New list is " + str(basket), "\n")