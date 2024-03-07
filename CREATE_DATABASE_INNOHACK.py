import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",password="tiger")
cursor=mydb.cursor()
cursor.execute("CREATE DATABASE INNOHACK")
