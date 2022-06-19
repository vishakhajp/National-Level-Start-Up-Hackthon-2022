from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX
import mysql.connector
#from numpy import meshgrid
import cv2


class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        

        # Top Image
        img_top=Image.open(r"college_images\attendance.jpeg")
        img_top=img_top.resize((1540,900), Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
 
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=0,width=1540,height=900)

        # Title Frame
        main_frame=Frame(self.root,bd=2,bg="green")
        main_frame.place(x=0, y=30,width=1540,height=55)

        title_lbl=Label(main_frame,text="HELP  DESK",font=("times new roman", 35, "bold"),bg="blue",fg="white")
        title_lbl.place(x=0, y=0,width=1530, height=50)


        # Help Lable
        help_label=Label(f_lbl, text="Email ID : vishakhalodha63@gmail.com", font=("times new roman", 30, "bold"),bg="#292929",fg="pink")
        help_label.place(x=410,y=200)


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()