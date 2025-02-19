import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='34.135.25.144',
                                         databae='mysql'
                                         user='root'
                                         passwor='')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySql server version", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You are connected to database:", record)
except Error as e:
    print("Error while connecting to MySql",e)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
