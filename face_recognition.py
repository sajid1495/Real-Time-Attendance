from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import mysql.connector 
import cv2
import os
import numpy as np


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        img = Image.open(r"images\face_recognition_bg.png")  
        img = img.resize((1540, 800), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_label = Label(self.root, image=self.photoimg)
        bg_label.place(x=0, y=0, width=1540, height=800)

        title_lbl = Label(bg_label, text="FACE RECOGNITION", font=("Calibri", 35, "bold"), bg="lavender", fg="red")
        title_lbl.place(x=0, y=0, width=1540, height=55)

        #button to start face recognition
        recognize_btn = Button(bg_label, text="Detect Face", command=self.face_recognize, font=("Helvetica", 14, "bold"), bg="red", fg="white", cursor="hand2")
        recognize_btn.place(x=1040, y=653, width=200, height=35)


    def face_recognize(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img(x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                if confidence > 77:
                    conn = mysql.connector.connect(host="localhost", username="root", password="password", database="face_recognition_db")
                    my_cursor = conn.cursor()

                    my_cursor.execute("select Name from student where StudentID=" + str(id))
                    n = my_cursor.fetchone()
                    name = "+".join(n)

                    my_cursor.execute("select Roll from student where StudentID=" + str(id))
                    r = my_cursor.fetchone()
                    roll = "+".join(r)

                    my_cursor.execute("select Department from student where StudentID=" + str(id))
                    d = my_cursor.fetchone()
                    department = "+".join(d)

                    cv2.putText(img, f"Name:{name}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{roll}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{department}", (x, y - 35), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord.append((x, y, w, h))

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()













if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()