import psycopg2
import os

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1713' #os.environ["password"]
DATABASE = 'avi_resto'

class MenuItem:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def update_item(self,**kwargs):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        setters = ""        
        for key,value in kwargs.items():
            setters += key + " = '" + str(value) + "',"
            setattr (self,key,value)
        setters = setters.rstrip(",")
        query = f"""UPDATE item 
                  set {setters}
                  where name = '{self.name}' ;"""
        print(query)
        cursor.execute(query)
        connection.commit()
        connection.close()

    def save(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"INSERT INTO item(name,price) VALUES ('{self.name}',{self.price})"
        cursor.execute(query)
        print(query)
        connection.commit()
        connection.close()

    def delete(self,name):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"DELETE FROM item WHERE name = '{self.name}'"
        cursor.execute(query)
        print(query)
        connection.commit()
        connection.close()
    @staticmethod
    def get_by_name(name):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"SELECT * FROM item WHERE name = '{name}'"
        cursor.execute(query)
        print(query)
        results = cursor.fetchall()
        if len(results) != 0 :
            print(results)
        else:
            print("None")
        connection.commit()
        connection.close()


def all():
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor()
        query = f"SELECT name  FROM item "
        cursor.execute(query)
        print(query)
        results = cursor.fetchall()
        print(results)
        connection.commit()
        connection.close()


    
# item1 = MenuItem("Burger",35)
# item2 = MenuItem("chips",70)
# item2.save()
#item2.delete('chips')
# item1.update_item(price=45)
# print(item1.price)
# all()
# MenuItem.get_by_name("kebab")

# /////////////////////////////////////////////
# EXERCISE 2 

