from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk 
import mysql.connector 
from time import strftime
from datetime import datetime
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


    #=========attendance function=========
    def mark_attendance(self, i, r, n, d):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            now = datetime.now()
            today_date = now.strftime("%d-%m-%Y")
            

            for line in myDataList:
                entry = line.strip().split(",")
                if len(entry) >= 5:
                    student_id = str(entry[0])
                    attendance_date = entry[4].split()[0] if " " in entry[4] else entry[4]
                    if str(i) == student_id and attendance_date == today_date:
                        return  

            dtString = now.strftime("%d-%m-%Y,%H:%M:%S")
            f.writelines(f"\n{i},{r},{n},{d},{dtString},Present")



    #=========face recognition function=========
    def face_recognize(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="sajid@96", database="face_recognition_attendance")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Student_id, Name, Roll, Dept FROM student")
            students = my_cursor.fetchall()
            conn.close()
            
            
            student_data = {}
            for student in students:
                try:
                    student_id = int(student[0])  
                except:
                    student_id = student[0]
                student_data[student_id] = {
                    "name": student[1],
                    "roll": student[2],
                    "dept": student[3]
                }
            
        except Exception as e:
            messagebox.showerror("Database Error", f"Could not connect to database: {e}")
            return
        
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))
                

                if id in student_data:
                    n = student_data[id]["name"]
                    r = student_data[id]["roll"]
                    d = student_data[id]["dept"]
                    i = id 
                else:
                    n, r, d = "Unknown", "N/A", "N/A"
 
                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    cv2.putText(img, f"Department:{d}", (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(img, "Unknown Face", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)

                coord.append((x, y, w, h))

            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
        
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open camera!")
            return
        
        cv2.namedWindow("Welcome TO face Recognition", cv2.WINDOW_NORMAL)
        
        while True:
            ret, img = video_cap.read()
            if not ret or img is None:
                continue  
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome TO face Recognition", img)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 13 or key == ord('q'):
                break


            if cv2.getWindowProperty("Welcome TO face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break
                
        video_cap.release()
        cv2.destroyAllWindows()













if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()