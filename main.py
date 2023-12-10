from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from students import Student



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"C:\Face Recognition System\Images\gla1.jpg")
        img=img.resize((500,130),Image.AFFINE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Face Recognition System\Images\Facial recognition.jpeg")
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
        title_lbl=Label(bg_image,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img4=Image.open(r"C:\Face Recognition System\Images\students.png")
        img4=img4.resize((220,220),Image.AFFINE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_image,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b2=Button(bg_image,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=300,width=220,height=40)

        #detect face
        img5=Image.open(r"C:\Face Recognition System\Images\Face detector.jpg")
        img5=img5.resize((220,220),Image.AFFINE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=220,height=220)

        b2=Button(bg_image,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=300,width=220,height=40)

        #Attendance 
        img6=Image.open(r"C:\Face Recognition System\Images\Attendance1.jpg")
        img6=img6.resize((220,220),Image.AFFINE)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_image,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b2=Button(bg_image,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=800,y=300,width=220,height=40)

        #help
        img7=Image.open(r"C:\Face Recognition System\Images\HelpDesk.jpeg")
        img7=img7.resize((220,220),Image.AFFINE)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_image,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=220,height=220)

        b2=Button(bg_image,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1100,y=300,width=220,height=40)

        #Train Software
        img8=Image.open(r"C:\Face Recognition System\Images\Train.jpg")
        img8=img8.resize((220,220),Image.AFFINE)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_image,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=380,width=220,height=220)

        b2=Button(bg_image,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=200,y=580,width=220,height=40)


        #Photos
        img9=Image.open(r"C:\Face Recognition System\Images\Gallery.jpeg")
        img9=img9.resize((220,220),Image.AFFINE)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_image,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=380,width=220,height=220,)

        b2=Button(bg_image,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=500,y=580,width=220,height=40)


        #Developer
        img10=Image.open(r"C:\Face Recognition System\Images\Developer.png")
        img10=img10.resize((220,220),Image.AFFINE)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_image,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=380,width=220,height=220)

        b2=Button(bg_image,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=800,y=580,width=220,height=40)


         #Exit
        img11=Image.open(r"C:\Face Recognition System\Images\Exit.jpg")
        img11=img11.resize((220,220),Image.AFFINE)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_image,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=380,width=220,height=220)

        b2=Button(bg_image,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2.place(x=1100,y=580,width=220,height=40)

##############Functions buttons ############

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)



















if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()