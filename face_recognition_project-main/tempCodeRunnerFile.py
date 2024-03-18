import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="PDss3921/*",
    database="global"
)
cur=conn.cursor()
sqlq="insert into student(name,usn,a_date,a_time) values(%s,%s,%s,%s)"