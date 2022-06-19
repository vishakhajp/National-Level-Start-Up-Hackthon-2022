from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from register import Register
import random
import time
import datetime
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()



class Login_window:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")

        #================ Variables ====================
        self.var_email=StringVar()
        self.var_pass=StringVar()

    

        self.bg=ImageTk.PhotoImage(file="college_images/hackers2.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0, y=0,relwidth=1,relheight=1)


        frame=Frame (self.root, bg="black")
        frame.place(x=600, y=170, width=340, height=450)

        img1=Image.open("college_images/LoginIconAppl.png")
        img1=img1.resize((100,100), Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730,y=180, width=100, height=100)


        get_str=Label(frame, text="Get Started", font=("times new roman", 20, "bold"),fg="white", bg="black")
        get_str.place(x=105,y=105)


        #label
        username=lbl=Label(frame, text="Username", font=("times new roman", 15, "bold"),fg="white", bg="black")
        username.place(x=78, y=155)

        self.txtuser=ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=180, width=270)

        password=lbl=Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=78,y=225)

        self.txtpass=ttk.Entry(frame, font=("times new roman", 15,"bold"))
        self.txtpass.place(x=40,y=250, width=270)


        #=====Icon Images====
        img2=Image.open(r"college_images\LoginIconAppl.png")
        img2=img2.resize((25,25), Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img3=Image.open(r"college_images\lock-512.png")
        img3=img3.resize( (25,25), Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage (img3)
        lblimg3=Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)


        #=========== Login Button =======================
        loginbtn=Button(frame, text="Login",command=self.login , font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110, y=300,width=120, height=35)

        #=========== Registration Button =======================
        registerbtn=Button(frame,command=self.rigister_window , text="New User Register", font=("times new roman", 15, "bold"), borderwidth=0 , fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=70, y=370,width=200, height=35)

        #=========== Forgot Password Button =======================
        loginbtn=Button(frame, text="Forgot Password?",command=self.forgot_password_window, font=("times new roman", 11, "bold"), borderwidth=0, fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=95, y=400,width=160, height=35)


    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)

        
    #===================== Login Functionality ========================

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.txtuser.get()=="vishakha" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success", "Welcome to Employee Attendance Management System")
        else:
            conn=mysql.connector.connect(host="localhost",user="root", password="123456", database="empl_face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                        self.txtuser.get(),
                                                                        self.txtpass.get()
                                                                ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Inavalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


    #========================== Reset Password ======================
    def reset_pass(self):
        if self.combo_securiy_Q.get()=="Select Question":
            messagebox.showerror("Error", "Select sucurity Quetion",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Plase enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="123456", database="empl_face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(), self.combo_securiy_Q.get(), self.txt_security.get(),)
            my_cursor.execute(query,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Plaese enter correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpass.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset ,plaese login with new password",parent=self.root2)
                self.root2.destroy()



    #========================== Forget Password ===================
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error", "Plaese Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="123456", database="empl_face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Plaese enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry ("340x450+600+170")


                l=Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"),fg="red", bg="white")
                l.place(x=0,y=10, relwidth=1)

                security_Q=Label(self.root2, text="Select Security Quetion", font=("times new roman",15, "bold"), bg="white",fg="black")
                security_Q.place(x=50, y=80)

                self.combo_securiy_Q=ttk.Combobox(self.root2, font=("times new roman",15, "bold"),state="readonly")
                self.combo_securiy_Q[ "values"]=("Select Question","Your Birth Place","Your Bestfriend name", "Your Pet Name")
                self.combo_securiy_Q.place(x=50,y=110, width=250)
                self.combo_securiy_Q.current(0)

                security_A=Label(self.root2,text="Security Answer", font=("times new roman",15, "bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2, font=("times new roman",15, "bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password", font=("times new roman",15,"bold"),bg="white", fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass=ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_newpass.place(x=50,y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass, font=("times new roman", 15, "bold"),fg="White",bg="green")
                btn.place(x=135, y=290)



if __name__=="__main__":
    main()

