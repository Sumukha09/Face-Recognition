import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PDss3921/*",
    database="global"
)
if conn.is_connected():
    print("connected")