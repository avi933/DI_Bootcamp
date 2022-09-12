from exerciseXp import MenuItem
import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1713' #os.environ["password"]
DATABASE = 'avi_resto'

# def load_manager():
#     connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
#     cursor = connection.cursor()
#     query = f"SELECT count('name') from item"
#     cursor.execute(query)
#     print(query)
#     results = cursor.fetchall()
#     print(results[0])
#     # item(result+1) = MenuItem(name,price)
#     # connection.commit()
#     connection.close()

# this function should display the program menu
# Call the appropriate function that matches the user’s input.
def show_user_menu():
    print("      Menu      ")
    print("(a)  Add an item")
    print("(d)  Delete an item")
    print("(v)  View an Menu")
    print("(x)  Exit\n")
    user = input("What operation you want to do?\n")
    if user == "a":
        confirm = input("You chose to add an item, press y to confirm or n to abort\n")
        if confirm == "n":
            print("You abort the add command")
            pass
        elif confirm == "y":
            m_name = input("Enter Menu Name\n")
            m_price = input("Enter the price of ",m_name, "\n")
            new_item = MenuItem(m_name,m_price)
            MenuItem.save(new_item)
            print(m_name," has successfully be saved")
        else:
            print("Error not a proper command")  

    if user == "v":
        confirm = input("You chose to view all item, press y to confirm or n to abort\n")
        if confirm == "n":
            print("You interrupted the view command")
            pass
        elif confirm == "y":
            
            print(all())
        else:
            print("Error not a proper command") 
    
    if user == "d":
        confirm = input("Are you sure you want to delete an item, press y to confirm or n to abort\n")
        if confirm == "n":
            print("Nothing was deleted")
            pass
        elif confirm == "y":
            MenuItem.delete()
            print("you deleted {self.name}")
        else:
            print("Error not a proper command") 

    if user == "x":
        confirm = input("Are you sure you want to EXIT, press y to confirm or n to abort\n")
        if confirm == "n":
            print("Thank for staying")
            pass
        elif confirm == "y":
            print("exiting the program")
            exit()
        else:
            print("Error not a proper command")


show_user_menu()


# load_manager()