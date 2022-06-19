from tkinter import*
from tkinter import ttk
from turtle import right, update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX
import mysql.connector
#from numpy import meshgrid
import cv2


class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        # Top Image
        img_top=Image.open(r"college_images\dev.jpg")
        img_top=img_top.resize((1540,900), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
 
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1540,height=900)

        # Title Frame
        main_frame=Frame(self.root,bd=2,bg="green")
        main_frame.place(x=0, y=30,width=1540,height=55)

        title_lbl=Label(main_frame,text="DEVELOPER",font=("times new roman", 35, "bold"),bg="blue",fg="white")
        title_lbl.place(x=0, y=0,width=1530, height=50)

        # Frame

        img_top1=Image.open(r"college_images\clock.jpg")
        img_top1=img_top1.resize((200,200), Image.ANTIALIAS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl_1=Label(f_lbl,image=self.photoimg_top1)
        f_lbl_1.place(x=1300, y=110,width=200, height=200)


        # Developer Information 

        dev_label=Label(f_lbl, text="Hello , My name is Vishakha !", font=("times new roman", 25, "bold"),bg="yellow",fg="green")
        dev_label.place(x=570,y=150)

        dev_label=Label(f_lbl, text="I'm a Student.  I study Computer Engineering.", font=("times new roman", 24, "bold"),bg="green",fg="pink")
        dev_label.place(x=450,y=220)  

       
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()