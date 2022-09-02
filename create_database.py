import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="eric",
  password="ericpython"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE face_recognition")