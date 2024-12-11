import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="MX4444mx",
        database="sakila",
        port="3306"
    )
    if mydb.is_connected():
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS avanc_database;")
        mycursor.execute("USE avanc_database;")
        mycursor.execute("SHOW DATABASES;")
        for x in mycursor.fetchall():
           print(x)

        table_name = "actor"  # specify your table name here
        mycursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );
        """)
    mycursor.execute(f"SELECT * FROM {table_name};")
    records = mycursor.fetchall()
    for record in records:
            print(record)

except Error as e:
    print(f"Error: {e}")

finally:
    if mydb.is_connected():
        mydb.close()
