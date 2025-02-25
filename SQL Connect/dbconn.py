import mysql.connector
from tabulate import tabulate

# install mysql_connector_python, tabulate

# if online, then write ip address. instead of localhost
conn = mysql.connector.connect(host="localhost", user="root", password="Google2020$", database="python_db")


# if conn:
#     print("Connected")
# else:
#     print("Connection Error")

# have to commit the conn then only it will be updated
# in db. insert delete and update
def insert(name, age, city):
    res = conn.cursor()
    sql = "insert into users (name,age,city) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql, user)  # parameters are passed here
    conn.commit()
    print("Data Inserted successfully")


def update(name, age, city, id):
    res = conn.cursor()
    sql = "update users set name = %s,age= %s,city= %s where id = %s"
    user = (name, age, city, id)
    res.execute(sql, user)  # parameters are passed here
    conn.commit()
    print("Data Updated successfully")


def select():
    # create a cursor object to sql conn. It like wire
    res = conn.cursor()
    sql = "SELECT * from users"
    res.execute(sql)
    # result = res.fetchone()
    # result = res.fetchmany(2)
    result = res.fetchall()
    # print(result)
    print(tabulate(result, headers=["ID", "NAME", "AGE", "CITY"]))


def delete(id):
    res = conn.cursor()
    sql = "delete from users where id = %s"
    user = (id,)
    res.execute(sql, user)  # parameters are passed here
    conn.commit()
    print("Data deleted successfully")



while True:
    print("1.Insert Data")
    print("2.Update Data")
    print("3.Select Data")
    print("4.Delete Data")
    print("5.Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        city = input("Enter the city: ")
        insert(name, age, city)
    elif choice == 2:
        id = int(input("Enter the Id: "))
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        city = input("Enter the city: ")
        update(name, age, city,id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter the id to delete: ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Choice. Please Try Again!")
