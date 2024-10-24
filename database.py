import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="chuen",
  password="c.c.c.c.c",
  database="GroceryShop"
)
print(mydb)
def newuser(newusername, newpassword):
    mycursor = mydb.cursor(dictionary = True)
    sql = "INSERT INTO Users (username, password, role) VALUES (%s, %s, %s)"
    val = (newusername, newpassword,"S")
    mycursor.execute(sql, val)
    mydb.commit()