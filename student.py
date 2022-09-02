from tkinter import* 
from tkinter import ttk
import mysql.connector
import cv2
from PIL import Image,ImageTk
from tkinter import messagebox


"""
conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
"""
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Student Pannel")

        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_mob=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

    # image-labeling 
        # 1st image header   
        img=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\banner.jpg")
        img=img.resize((1366,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        # setting image as a lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

         # image for backgorund  
        bg1=Image.open(r"C:\Users\Reekado\Desktop\final\SFAMS\Images_GUI\bg3.jpg")
        bg1=bg1.resize((1366,768),Image.ANTIALIAS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # setting image as a lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        # section-title 
        title_lb1 = Label(bg_img,text="Welcome to Student Enrollment",font=("verdana",25,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # frame-Creation 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # labeling-Left-Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=660,height=480)

        # Current-Course 
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("verdana",12,"bold"),fg="navyblue")
        current_course_frame.place(x=10,y=5,width=635,height=150)

        # labelling-the-Department
        dep_label=Label(current_course_frame,text="Department",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        dep_label.grid(row=0,column=0,padx=5,pady=15)

        # combobox 
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,width=15,font=("verdana",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Faculty of Arts and Humanities","Faculty of Engineering,Environment and Computing","Faculty of Health and Life Sciences","Faculty of Business and Law")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)


        # Course-labelling
        cou_label=Label(current_course_frame,text="Course",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        cou_label.grid(row=0,column=2,padx=5,pady=15)

        # combobox 
        cou_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,width=15,font=("verdana",12,"bold"),state="readonly")
        cou_combo["values"]=("Select Course","Automotive and Transport Design BA (Hons)","Fashion BA (Hons)","Architecture MA","Graphic Design MA","History MA","Politics MA","English BA(Hons)","Sociology and Criminology BA(Hons","Computer SCience BSc(Hons)","Data Science BSc(Hons)","Cyber Security MSc","Software Development Msc","Midwifery BSc(Hons)","Paramedic Science Bsc(Hons)","Nursing MSc","Public Health Nutrition Msc","Sport Coaching BSc(Hons)","Human Biosciences BSc(Hons)","Accounting and Finance BSc(Hons)","Advertising Marketing BA(Hons)")
        cou_combo.current(0)
        cou_combo.grid(row=0,column=3,padx=5,pady=15,sticky=W)


        # Year-labelling
        year_label=Label(current_course_frame,text="Year",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=0,padx=5,sticky=W)

        # year-combobox 
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2017-21","2018-22","2019-23","2020-24","2021-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=15,sticky=W)


        # semister-labelling
        year_label=Label(current_course_frame,text="Semester",font=("verdana",12,"bold"),bg="white",fg="navyblue")
        year_label.grid(row=1,column=2,padx=5,sticky=W)

        #comboo-box
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,width=15,font=("verdana",12,"bold"),state="readonly")
        year_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=15,sticky=W)

        # student-information
        class_Student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",12,"bold"),fg="navyblue")
        class_Student_frame.place(x=11,y=161,width=636,height=231)

        # student id labelling
        studentId_label = Label(class_Student_frame,text="Std-ID:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
         
        studentId_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=15,font=("verdana",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #student-name label
        student_name_label = Label(class_Student_frame,text="Std-Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        # division-classion
        student_div_label = Label(class_Student_frame,text="Class Division:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,width=13,font=("verdana",12,"bold"),state="readonly")
        div_combo["values"]=("Morning","Evening")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        # Roll-No
        student_roll_label = Label(class_Student_frame,text="Roll-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        student_roll_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        # Genderr
        student_gender_label = Label(class_Student_frame,text="Gender:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_gender_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        # combo-box 
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        # DOB
        student_dob_label = Label(class_Student_frame,text="DOB:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_dob_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        student_dob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=15,font=("verdana",12,"bold"))
        student_dob_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # Email-Address
        student_email_label = Label(class_Student_frame,text="Email:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_email_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        student_email_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        # Phone-No
        student_mob_label = Label(class_Student_frame,text="Mob-No:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_mob_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame,textvariable=self.var_mob,width=15,font=("verdana",12,"bold"))
        student_mob_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        # Address-label
        student_address_label = Label(class_Student_frame,text="Address:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_address_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        student_address_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        # Teacher-Name
        student_tutor_label = Label(class_Student_frame,text="Tutor Name:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_tutor_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=15,font=("verdana",12,"bold"))
        student_tutor_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        # Radio Buttons for take photo sample and no photo sample
        self.var_radio1=StringVar()
        radiobtn_1=ttk.Radiobutton(class_Student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn_1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn_1=ttk.Radiobutton(class_Student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn_1.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        # frame Button 
        btn_frame_ = Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame_.place(x=10,y=390,width=635,height=60)

        # button to save 
        save_btn=Button(btn_frame_,command=self.add_data,text="Save",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        # button for update 
        update_btn=Button(btn_frame_,command=self.update_data,text="Update",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        # btn-delete 
        del_btn=Button(btn_frame_,command=self.delete_data,text="Delete",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        # btn-reset 
        reset_btn=Button(btn_frame_,command=self.reset_data,text="Reset",width=7,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        # btn-taking photo
        take_photo_btn=Button(btn_frame_,command=self.generate_dataset,text="Take Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)

        #btn-updating photo 
        update_photo_btn=Button(btn_frame_,text="Update Pic",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)





        
        # Right-Label-Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("verdana",12,"bold"),fg="navyblue")
        right_frame.place(x=681,y=11,width=661,height=481)

        # Searching-System-Right-Label-Frame 
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("verdana",12,"bold"),fg="navyblue")
        search_frame.place(x=11,y=6,width=636,height=81)

        # Phone-Num-label
        search_label = Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        self.var_searchTX=StringVar()
        # combo-boox 
        search_combo_=ttk.Combobox(search_frame,textvariable=self.var_searchTX,width=12,font=("verdana",12,"bold"),state="readonly")
        search_combo_["values"]=("Select","Roll-No")
        search_combo_.current(0)
        search_combo_.grid(row=0,column=1,padx=5,pady=15,sticky=W)

        self.var_search=StringVar()
        search_entry_ = ttk.Entry(search_frame,textvariable=self.var_search,width=12,font=("verdana",12,"bold"))
        search_entry_.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        search_btn=Button(search_frame,command=self.search_data,text="Search",width=9,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        showAll_btn_=Button(search_frame,command=self.fetch_data,text="Show All",width=8,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        showAll_btn_.grid(row=0,column=4,padx=5,pady=10,sticky=W)

       
        
        # Searching-System-Right Label Frame 
        table_framee = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_framee.place(x=10,y=90,width=635,height=360)

        # scroll-bar 
        scroll_x = ttk.Scrollbar(table_framee,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_framee,orient=VERTICAL)

        # create-table 
        self.student_table_ = ttk.Treeview(table_framee,column=("ID","Name","Dep","Course","Year","Sem","Div","Gender","DOB","Mob-No","Address","Roll-No","Email","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table_.xview)
        scroll_y.config(command=self.student_table_.yview)

        self.student_table_.heading("ID",text="StudentID.")
        self.student_table_.heading("Name",text="Name.")
        self.student_table_.heading("Dep",text="Department.")
        self.student_table_.heading("Course",text="Course.")
        self.student_table_.heading("Year",text="Year.")
        self.student_table_.heading("Sem",text="Semester.")
        self.student_table_.heading("Div",text="Division.")
        self.student_table_.heading("Gender",text="Gender.")
        self.student_table_.heading("DOB",text="DOB.")
        self.student_table_.heading("Mob-No",text="Mob-No.")
        self.student_table_.heading("Address",text="Address.")
        self.student_table_.heading("Roll-No",text="Roll-No.")
        self.student_table_.heading("Email",text="Email.")
        self.student_table_.heading("Teacher",text="Teacher.")
        self.student_table_.heading("Photo",text="PhotoSample.")
        self.student_table_["show"]="headings"


        # Setting Width of Columns 
        self.student_table_.column("ID",width=101)
        self.student_table_.column("Name",width=101)
        self.student_table_.column("Dep",width=101)
        self.student_table_.column("Course",width=101)
        self.student_table_.column("Year",width=101)
        self.student_table_.column("Sem",width=101)
        self.student_table_.column("Div",width=101)
        self.student_table_.column("Gender",width=101)
        self.student_table_.column("DOB",width=101)
        self.student_table_.column("Mob-No",width=101)
        self.student_table_.column("Address",width=101)
        self.student_table_.column("Roll-No",width=101)
        self.student_table_.column("Email",width=101)
        self.student_table_.column("Teacher",width=101)
        self.student_table_.column("Photo",width=101)


        self.student_table_.pack(fill=BOTH,expand=1)
        self.student_table_.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

# Function-Declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                
                mycursor.execute("insert into student (Name,\
Department,\
Course,\
Year,\
Semester,\
Division,\
Gender,\
DOB,\
Mobile_No,\
Address,\
Roll_No,\
Email,\
Teacher_Name)" 
"values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                self.var_std_name.get(),
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_mob.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    # fetch data from database to the table 

    def fetch_data(self):
        conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table_.delete(*self.student_table_.get_children())
            for i in data:
                self.student_table_.insert("",END,values=i)
            conn.commit()
        conn.close()

    #  function to get cursor_

    def get_cursor(self,event=""):
        cursor_focus_ = self.student_table_.focus()
        content = self.student_table_.item(cursor_focus_)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_mob.set(data[9]),
        self.var_address.set(data[10]),
        self.var_roll.set(data[11]),
        self.var_email.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # Function-Update
    ## update all the data of student
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
     
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    #Function-Delete
    ## this deletes any records requiered to delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id is Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Are you sure you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete"," Deletedd Successfully!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    # Function-reset 
    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_div.set("Morning"),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    
    # Searching-Data
    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="Select":
            messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
                my_cursor = conn.cursor()
                sql = "SELECT Student_ID,Name,Department,Course,Year,Semester,Division,Gender,DOB,Mobile_No,Address,Roll_No,Email,Teacher_Name,PhotoSample FROM student where Roll_No='" +str(self.var_search.get()) + "'" 
                my_cursor.execute(sql)
                rows=my_cursor.fetchall()        
                if len(rows)!=0:
                    self.student_table_.delete(*self.student_table_.get_children())
                    for i in rows:
                        self.student_table_.insert("",END,values=i)
                    if rows==None:
                        messagebox.showerror("Error","Dataa Not Found",parent=self.root)
                        conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Duee To :{str(es)}",parent=self.root)



    # Generating Dataset to capture image, so it could be used for data training
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_mob.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are Required!",parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='eric', password='ericpython',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Gender=%s,DOB=%s,Mobile_No=%s,Address=%s,Roll_No=%s,Email=%s,Teacher_Name=%s,PhotoSample=%s where Student_ID=%s",( 
                    self.var_std_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_mob.get(),
                    self.var_address.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # opencv

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # converting to garysacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces_ = face_classifier.detectMultiScale(gray,1.3,5)
                    
                    #finding faces
                    for (x,y,w,h) in faces_:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                capp=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=capp.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face_=cv2.resize(face_croped(my_frame),(200,200))
                        face_=cv2.cvtColor(face_,cv2.COLOR_BGR2GRAY)
                        file_path="data_img/stdudent."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face_)
                        cv2.putText(face_,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face_)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                capp.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating the dataset  is now completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 


# main

if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
