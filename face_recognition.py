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
        # Connect to database once and cache student data
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="sajid@96", database="face_recognition_attendance")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Student_id, Name, Roll, Dept FROM student")
            students = my_cursor.fetchall()
            conn.close()
            
            # Create a dictionary for fast lookup (convert Student_id to int for matching)
            student_data = {}
            for student in students:
                try:
                    student_id = int(student[0])  # Convert to int to match classifier output
                except:
                    student_id = student[0]
                student_data[student_id] = {
                    "name": student[1],
                    "roll": student[2],
                    "dept": student[3]
                }
            print(f"Loaded {len(student_data)} students: {list(student_data.keys())}")  # Debug info
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
                
                print(f"Detected ID: {id}, Confidence: {confidence}")  # Debug info

                # Get student info from cached data
                if id in student_data:
                    n = student_data[id]["name"]
                    r = student_data[id]["roll"]
                    d = student_data[id]["dept"]
                else:
                    n, r, d = "Unknown", "N/A", "N/A"
 
                if confidence > 77:
                    cv2.putText(img, f"Roll:{r}", (x, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
                    cv2.putText(img, f"Department:{d}", (x, y - 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 180, 230), 2)
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

        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow on Windows
        
        # Check if camera opened successfully
        if not video_cap.isOpened():
            messagebox.showerror("Error", "Could not open camera!")
            return
        
        # Create a named window and bring it to front
        cv2.namedWindow("Welcome TO face Recognition", cv2.WINDOW_NORMAL)
        
        while True:
            ret, img = video_cap.read()
            if not ret or img is None:
                continue  # Skip frame if not read properly
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome TO face Recognition", img)
            
            # Wait for key press - 'Enter' key (13) or 'q' to quit
            key = cv2.waitKey(1) & 0xFF
            if key == 13 or key == ord('q'):
                break
            
            # Check if window was closed by clicking X button
            if cv2.getWindowProperty("Welcome TO face Recognition", cv2.WND_PROP_VISIBLE) < 1:
                break
                
        video_cap.release()
        cv2.destroyAllWindows()













if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()