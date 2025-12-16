from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Background Image
        img = Image.open(r"images\bg.png")  
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_image = Label(self.root, image=self.photoimg)
        bg_image.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_image, text="REAL TIME ATTENDANCE SYSTEM SOFTWARE", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
        title_lbl.place(x=0, y=0, width=1540, height=55)


        #students button
        student = Image.open(r"images\students.png")  
        student = student.resize((220, 220), Image.Resampling.LANCZOS)
        self.photostudent = ImageTk.PhotoImage(student)

        btn1 = Button(bg_image, image=self.photostudent, cursor="hand2")
        btn1.place(x=200, y=100, width=220, height=220)

        btn1_text = Button(bg_image, text="Students Details", cursor="hand2", font=("Calibri", 16, "bold"))
        btn1_text.place(x=200, y=320, width=220, height=40)


        #detect face button
        detect_face = Image.open(r"images\detect_faces.png")  
        detect_face = detect_face.resize((220, 220), Image.Resampling.LANCZOS)
        self.photodetect_face = ImageTk.PhotoImage(detect_face)

        btn1 = Button(bg_image, image=self.photodetect_face, cursor="hand2")
        btn1.place(x=450, y=100, width=220, height=220)

        btn1_text = Button(bg_image, text="Detect Face", cursor="hand2", font=("Calibri", 16, "bold"))
        btn1_text.place(x=450, y=320, width=220, height=40)
        

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()