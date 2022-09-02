from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
mycursor = conn.cursor()
query=("SELECT * FROM register")
#value=(self.var_email.get(),)
mycursor.execute(query)
row=mycursor.fetchall()
print(row)
if row==None:
    messagebox.showerror("Error","nothing found")
else:
    print("something found")
    print(row)
    
conn.commit()
conn.close()