from tkinter import* 
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk


import mysql.connector
from register import Register
from train import Train
from helpsupport import Helpsupport
from face_recognition import Face_Recognition
from attendance import Attendance
from student import Student
from train import Train
from developer import Developer
import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")

        # variablesss 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\loginBg1.jpg")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=561,y=171,width=341,height=451)

        img1=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\log1.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="#002B53")
        lb1img1.place(x=691,y=176, width=101,height=101)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=141,y=101)

        #label-1
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=31,y=161)

        #entry-1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=34,y=191,width=271)


        #label-2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=31,y=231)

        #entry-2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=34,y=261,width=271)


        # Creatingg BTN for Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=34,y=321,width=271,height=36)


        # Creatingg BTN fot Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=34,y=371,width=51,height=21)


        # Creating BTN for Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=91,y=371,width=50,height=20)


    #  Function for opening register windoww
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    # function to loggin 
    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # check for username and password
            conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
            m_cursor = conn.cursor()
            m_cursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=m_cursor.fetchone()
            # if no records found then show error
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#########Reset-Passowrd-Function######
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Please Select the Security Question.",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Enter the Answer.",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Enter  New Password.",parent=self.root2)
        else:
            conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Enter Correct Answer.",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been rest, login with new Password.",parent=self.root2)
                



#############Forget window############
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Enter the Email to Reset Password!")
        else:
            conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
            m_cursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            m_cursor.execute(query,value)
            row=m_cursor.fetchone()
           

            if row==None:
                messagebox.showerror("Error","Enter the Valid Email.")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forgot Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)

                # ---fields-
                #label-1
                ssq =lb1= Label(self.root2,text="Please Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=71,y=81)

                #Combo-Box-1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your DOB","Your Nick-Name","Your Favorite-Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label-2 
                sa =lb1= Label(self.root2,text="Securityy Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=71,y=151)

                #entry-2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=71,y=181,width=270)

                #label-2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry-2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Cretting BTN for New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=71,y=301,width=271,height=36)


            

# #####Main program Face detection system ########

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face_Recogonition_System")

# This part is setting image labelling

        # 1st header img
        img=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # setting image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund-image 
        bg1=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # setting image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title-section
        title_lb1 = Label(bg_img,text="Student Facial Recognition Attendance Management System",font=("verdana",25,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create BTN below the section 

        # student BTN 
        std_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\std1.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.ANTIALIAS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2")
        std_b1.place(x=251,y=101,width=181,height=181)

        std_b1_1 = Button(bg_img,command=self.student_pannels,text="Enrol New Student",cursor="hand2",font=("tahoma",13,"bold"),bg="navyblue",fg="white")
        std_b1_1.place(x=251,y=281,width=181,height=46)

        # Detect-Face  BTN
        det_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\det1.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.ANTIALIAS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=481,y=101,width=181,height=181)

        det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("tahoma",13,"bold"),bg="navyblue",fg="white")
        det_b1_1.place(x=480,y=280,width=180,height=45)

         # Attendance-System  BTN 
        att_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\att.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.ANTIALIAS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=711,y=101,width=181,height=181)

        att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("tahoma",13,"bold"),bg="navyblue",fg="white")
        att_b1_1.place(x=711,y=281,width=181,height=46)

         # Help  Support  BTN
        hlp_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\hlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.ANTIALIAS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=941,y=101,width=181,height=181)

        hlp_b1_1 = Button(bg_img,text="Help Support",cursor="hand2",font=("tahoma",13,"bold"),bg="navyblue",fg="white")
        hlp_b1_1.place(x=941,y=281,width=181,height=46)

        
        # Startting below BTNS
         # Train- btn
        tra_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\tra1.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.ANTIALIAS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",)
        tra_b1.place(x=251,y=331,width=181,height=181)

        tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Data",cursor="hand2",font=("tahoma",13,"bold"),bg="navyblue",fg="white")
        tra_b1_1.place(x=251,y=511,width=181,height=46)

        # Photo-button
        pho_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\qr1.png")
        pho_img_btn=pho_img_btn.resize((180,180),Image.ANTIALIAS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",)
        pho_b1.place(x=481,y=331,width=181,height=181)

        pho_b1_1 = Button(bg_img,command=self.open_img,text="QR-Codes",cursor="hand2",font=("tahoma",13,"bold"),bg="navyblue",fg="white")
        pho_b1_1.place(x=481,y=511,width=181,height=46)

        # Developers   BTN 
        dev_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\dev.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.ANTIALIAS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",)
        dev_b1.place(x=711,y=331,width=181,height=181)

        dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("tahoma",13,"bold"),bg="navyblue",fg="white")
        dev_b1_1.place(x=711,y=511,width=181,height=46)

        # exit   btn
        exi_img_btn=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\exi.jpg")
        exi_img_btn=exi_img_btn.resize((180,180),Image.ANTIALIAS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(bg_img,image=self.exi_img1,cursor="hand2",)
        exi_b1.place(x=941,y=331,width=181,height=181)

        exi_b1_1 = Button(bg_img,text="Exit",cursor="hand2",font=("tahoma",13,"bold"),bg="navyblue",fg="white")
        exi_b1_1.place(x=941,y=511,width=181,height=46)

# ##############Funtion forr Open IMGS Folder###########
    def open_img(self):
        os.startfile("data_img")


# #########Functions Buttons############
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
  
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def open_img(self):
        os.startfile("dataset")
    
  




if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()