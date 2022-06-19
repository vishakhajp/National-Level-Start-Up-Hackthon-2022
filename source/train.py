from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image,ImageTk
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        # Top Image
        img_top=Image.open(r"college_images\smart_city.jpg")
        img_top=img_top.resize((1540,900), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
 
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1540,height=900)

        # Title Frame
        main_frame=Frame(self.root,bd=2,bg="green")
        main_frame.place(x=0, y=30,width=1540,height=55)

        title_lbl=Label(main_frame,text="TRAIN DATASET",font=("times new roman", 35, "bold"),bg="darkblue",fg="powder blue")
        title_lbl.place(x=0, y=0,width=1530, height=50)


        # Center Button
        b1_1=Button(self.root,text="TRAIN DATA" , command=self.train_classifier , cursor="hand2",font=("times new roman", 25 , "bold"),bg="red",fg="white")
        b1_1.place(x=520, y=370,width=500,height=50)


    #=================================== Train Data ========================================

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #====================== Train the classifier And save==================================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!",parent=self.root)
                
                



if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()