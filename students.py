from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


       # ========variables=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob= StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        #first image
        img=Image.open(r"C:\Face Recognition System\Images\gla1.jpg")
        img=img.resize((500,130),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Face Recognition System\Images\students1.jpg")
        img1=img1.resize((500,130),Image.AFFINE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)

        #third image
        img2=Image.open(r"C:\Face Recognition System\Images\gla1.jpg")
        img2=img2.resize((500,130),Image.AFFINE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

        #bg image
        img3=Image.open(r"C:\Face Recognition System\Images\bg image.jpg")
        img3=img3.resize((1530,710),Image.AFFINE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_image=Label(self.root,image=self.photoimg3)
        bg_image.place(x=0,y=130,width=1530,height=710)


        #label title
        title_lbl=Label(bg_image,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        #frame
        main_frame=Frame(bg_image,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)


        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=580)

        #image in left frame
        img_left=Image.open(r"C:\Face Recognition System\Images\gla_students.jpg")
        img_left=img_left.resize((720,130),Image.AFFINE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)



        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=150)


        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=17,state="readonly")
        dep_combo['values']=("Select Department","Computer Science","IT","Civil","Mechanical","EC","Law")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)



        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo['values']=("Select Course","B.Tech","BCA","MCA","BA.LLB")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo['values']=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo['values']=("Select Semester","1","2","3","4","5","6","7","8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="CLass Student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)


        #studentID
        studentID_label=Label(class_student_frame,text="Student ID",font=("times new roman",13,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class div
        class_div_label=Label(class_student_frame,text="Section:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Gender
        Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=20,state="readonly")
        gender_combo['values']=("Select","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)


        #DOB

        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phoneNo
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #Address
        address_label=Label(class_student_frame,text="Address::",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


         #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take a photo sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No photo sample",value="No")
        radiobtn2.grid(row=6,column=1)


        #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)


        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)


        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #second frame
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=245,width=715,height=35)


        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)


        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=30,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)





        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=760,y=10,width=730,height=580)


        img_right=Image.open(r"C:\Face Recognition System\Images\students2.jpg")
        img_right=img_right.resize((720,130),Image.AFFINE)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)




        #Search System

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=720,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="Black",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo['values']=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=4,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=5,padx=4)

        ###################TABLE FRAME ###############################
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=720,height=350)



        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side= RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"


        self.student_table.column("dep",width="100")
        self.student_table.column("course",width="100")
        self.student_table.column("year",width="100")
        self.student_table.column("sem",width="100")
        self.student_table.column("id",width="100")
        self.student_table.column("name",width="100")
        self.student_table.column("div",width="100")
        self.student_table.column("roll",width="100")
        self.student_table.column("gender",width="100")
        self.student_table.column("dob",width="100")
        self.student_table.column("email",width="100")
        self.student_table.column("phone",width="100")
        self.student_table.column("address",width="100")
        self.student_table.column("teacher",width="100")
        self.student_table.column("photo",width="150")

        self.student_table.pack (fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        

    # ==========================Function Decleration======================
    def add_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.va_std_id.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="8650@vikas",database="face_recognizer")
                mycursor=conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.va_std_id.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()


                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    ###############fetch data###############

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="8650@vikas",database="face_recognizer")
        mycursor=conn.cursor()
        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


     #############get cursor###################
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data [3]), 
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]), 
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


###################update function################

    def update_data(self):
        if (
            self.var_dep.get() == "Select Department"
            or self.var_std_name.get() == ""
            or self.va_std_id.get() == ""  
        ):
            messagebox.showerror("Error", "All Fields are required", parent=self.root)

        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="8650@vikas",
                        database="face_recognizer"
                    )
                    mycursor = conn.cursor()
                    mycursor.execute("UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details updated", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
























if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()