from tkinter import*
from tkinter import ttk
from sys import path
import mysql.connector
import cv2
from PIL import Image,ImageTk
import os
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Train Section")

        # img label
        # 1st image headerr
        img=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # setting image as a lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # image-backgorund
        bg1=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\t_bg1.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # setting- lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=131,width=1366,height=768)


        # title-labele 
        title_lb1 = Label(bg_img,text="Training Dataset",font=("verdana",25,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1367,height=45)

      
        
        # btn for training data
        std_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\t_btn1.png")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=601,y=171,width=181,height=181)

        std_b1_1 = Button(bg_img,command=self.train_classifier,text="Train Dataset",cursor="hand2",font=("tahoma",15,"bold"),bg="navyblue",fg="white")
        std_b1_1.place(x=601,y=351,width=181,height=46)

    # Training-Function
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        facess=[]
        ids_=[]

        for img in path:
            img=Image.open(img).convert('L') # converting into grayscale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(img)[1].split('.')[1])

            facess.append(imageNp)
            ids_.append(id)
            print("HEEEEEEEYOOOOOOOOOO")
            print(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids_=np.array(ids_)
        
        # Training-Classifier
        clf= cv2.face.LBPHFaceRecognizer_create()
        clf.train(facess,ids_)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset is now Completed!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()