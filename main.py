from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from student import Student


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Background Image
        img = Image.open(r"images\_bg.png")  
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_image, text="REAL TIME ATTENDANCE SYSTEM SOFTWARE", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
        title_lbl.place(x=0, y=0, width=1540, height=55)


        #students button
        student = Image.open(r"images\students.png")  
        student = student.resize((180, 180), Image.Resampling.LANCZOS)
        self.photostudent = ImageTk.PhotoImage(student)

        btn1 = Button(bg_image, image=self.photostudent, command=self.student_details , cursor="hand2") 
        btn1.place(x=255, y=130, width=180, height=180)

        btn1_text = Button(bg_image, text="Students Details", command=self.student_details , cursor="hand2", font=("Calibri", 14, "bold"))
        btn1_text.place(x=255, y=310, width=180, height=40)


        #detect face button
        detect_face = Image.open(r"images\detect_faces.png")  
        detect_face = detect_face.resize((180, 180), Image.Resampling.LANCZOS)
        self.photodetect_face = ImageTk.PhotoImage(detect_face)

        btn2 = Button(bg_image, image=self.photodetect_face, cursor="hand2")
        btn2.place(x=535, y=130, width=180, height=180)

        btn2_text = Button(bg_image, text="Face Detector", cursor="hand2", font=("Calibri", 14, "bold"))
        btn2_text.place(x=535, y=310, width=180, height=40)

        #attendance button
        attendance = Image.open(r"images\attendance.png")  
        attendance = attendance.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoattendance = ImageTk.PhotoImage(attendance)

        btn3 = Button(bg_image, image=self.photoattendance, cursor="hand2")
        btn3.place(x=815, y=130, width=180, height=180)

        btn3_text = Button(bg_image, text="Attendance", cursor="hand2", font=("Calibri", 14, "bold"))
        btn3_text.place(x=815, y=310, width=180, height=40)

        #train data button
        traindata = Image.open(r"images\train_data.png")  
        traindata = traindata.resize((180, 180), Image.Resampling.LANCZOS)
        self.phototraindata = ImageTk.PhotoImage(traindata)

        btn4 = Button(bg_image, image=self.phototraindata, cursor="hand2")
        btn4.place(x=1095, y=130, width=180, height=180)

        btn4_text = Button(bg_image, text="Train Data", cursor="hand2", font=("Calibri", 14, "bold"))
        btn4_text.place(x=1095, y=310, width=180, height=40)

        #photos button
        photos = Image.open(r"images\photos.png")  
        photos = photos.resize((180, 180), Image.Resampling.LANCZOS)
        self.photophotos = ImageTk.PhotoImage(photos)

        btn5 = Button(bg_image, image=self.photophotos, cursor="hand2")
        btn5.place(x=255, y=420, width=180, height=180)

        btn5_text = Button(bg_image, text="Photoes", cursor="hand2", font=("Calibri", 14, "bold"))
        btn5_text.place(x=255, y=600, width=180, height=40)

        #help desk button
        helpdesk = Image.open(r"images\help_desk.png")   
        helpdesk = helpdesk.resize((180, 180), Image.Resampling.LANCZOS)
        self.photohelpdesk = ImageTk.PhotoImage(helpdesk)

        btn6 = Button(bg_image, image=self.photohelpdesk, cursor="hand2")
        btn6.place(x=535, y=420, width=180, height=180)

        btn6_text = Button(bg_image, text="Help Desk", cursor="hand2", font=("Calibri", 14, "bold"))
        btn6_text.place(x=535, y=600, width=180, height=40)

        #developer button
        developer = Image.open(r"images\developer.png")   
        developer = developer.resize((180, 180), Image.Resampling.LANCZOS)
        self.photodeveloper = ImageTk.PhotoImage(developer)

        btn7 = Button(bg_image, image=self.photodeveloper, cursor="hand2")
        btn7.place(x=815, y=420, width=180, height=180)

        btn7_text = Button(bg_image, text="Developer", cursor="hand2", font=("Calibri", 14, "bold"))
        btn7_text.place(x=815, y=600, width=180, height=40)

        #exit button
        exitbtn = Image.open(r"images\exit.png")   
        exitbtn = exitbtn.resize((180, 180), Image.Resampling.LANCZOS)
        self.photoexit = ImageTk.PhotoImage(exitbtn)

        btn8 = Button(bg_image, image=self.photoexit, cursor="hand2")
        btn8.place(x=1095, y=420, width=180, height=180)

        btn8_text = Button(bg_image, text="Exit", cursor="hand2", font=("Calibri", 14, "bold"))
        btn8_text.place(x=1095, y=600, width=180, height=40)
        

    #button function
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

















if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()