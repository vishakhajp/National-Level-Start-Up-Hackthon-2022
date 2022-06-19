from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX
import mysql.connector
#from numpy import meshgrid
import cv2


class Employee:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")


        #============================ Variables ====================================

        
        self.var_emp_id=StringVar()
        self.var_emp_name=StringVar()
        self.var_dep=StringVar()
        self.var_dep_id=StringVar()
        self.var_date=StringVar()
        self.var_proof_type=StringVar()
        self.var_proof_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()



        # first Image
        img=Image.open(r"college_images\shine.jpg")
        img=img.resize((400,150), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
 
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)
 
        # Second Image
        img1=Image.open(r"college_images\shine.jpg")
        img1=img1.resize((400,130), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
 
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=400,height=130)
 
        # Third Image
        img2=Image.open(r"college_images\shine.jpg")
        img2=img2.resize((400,150), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
 
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=400,height=130)

        # fourth Image
        img_2=Image.open(r"college_images\shine.jpg")
        img_2=img_2.resize((400,150), Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)
 
        f_lbl=Label(self.root,image=self.photoimg_2)
        f_lbl.place(x=1200,y=0,width=400,height=130)


        # Title Frame
        main_frame=Frame(self.root,bd=2,bg="green")
        main_frame.place(x=0, y=30,width=1540,height=55)

        title_lbl=Label(main_frame,text="EMPLOYEE  MANAGEMENT  SYSTEM",font=("times new roman", 35, "bold"),bg="blue",fg="white")
        title_lbl.place(x=0, y=0,width=1530, height=50)


        # bg Image
        img3=Image.open(r"college_images\back.jpg")
        img3=img3.resize((1540,710), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
 
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1540,height=710)
 
    
        # Left label frame
        Left_frame=LabelFrame(bg_img, bd=15,bg="cyan", relief=RIDGE, font=("times new roman",12,"bold"))
        Left_frame.place(x=30, y=60,width=770,height=585)

        dep_label_1=Label(Left_frame, text="Employee Information", font=("times new roman", 20, "bold"),bg="cyan",fg="black")
        dep_label_1.place(x=280,y=0,width=270,height=50)

        # Current dep_id information
        current_dep_id_frame=LabelFrame(Left_frame, bd=10, relief=RIDGE, text=" Employee Department Information ", font=("times new roman",15,"bold"),bg="white",fg="black")
        current_dep_id_frame.place(x=8, y=55,width=725,height=130)

        # Department
        dep_label=Label(current_dep_id_frame, text="Department :", font=("times new roman", 12, "bold"),bg="white",fg="black")
        dep_label.grid(row=0, column=0,padx=20,sticky=W)

        dep_combo=ttk.Combobox(current_dep_id_frame, textvariable=self.var_dep , font=("times new roman", 12, "bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department", "HR", "Manager", "CEO")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Dep_id
        dep_id_label=Label(current_dep_id_frame, text="Department ID :", font=("times new roman", 12, "bold"),bg="white",fg="black")
        dep_id_label.grid(row=0, column=2,padx=20,sticky=W)

        dep_id_combo=ttk.Combobox(current_dep_id_frame , textvariable=self.var_dep_id , font=("times new roman", 12, "bold"),state="readonly",width=20)
        dep_id_combo["values"]=("Select ID", "201", "405", "302","701")
        dep_id_combo.current(0)
        dep_id_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Date
        date_label=Label(current_dep_id_frame, text="Date of Joining :", font=("times new roman", 12, "bold"),bg="white",fg="black")
        date_label.grid(row=1, column=0,padx=20,sticky=W)

        date_combo=ttk.Combobox(current_dep_id_frame , textvariable=self.var_date , font=("times new roman", 12, "bold"),state="readonly",width=20)
        date_combo["values"]=("Select Date", "21-06-2022", "22-06-2022", "23-06-2022","24-06-2022")
        date_combo.current(0)
        date_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        
        # Class employee information
        class_employee_frame=LabelFrame(Left_frame, bd=10, relief=RIDGE, text=" Employee Personal Information ", font=("times new roman",15,"bold"),bg="white",fg="black")
        class_employee_frame.place(x=8, y=195,width=725,height=278)

        # Employee ID
        employeeID_label=Label(class_employee_frame, text="Employee ID :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        employeeID_label.grid(row=0, column=0,padx=10,pady=10,sticky=W)

        employeeID_entry=ttk.Entry(class_employee_frame , textvariable=self.var_emp_id , width=20, font=("times new roman", 13, "bold"))
        employeeID_entry.grid (row=0, column=1, padx=10, pady=5, sticky=W)

        # Employee Name
        studenName_label=Label(class_employee_frame, text="Employee Name :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        studenName_label.grid(row=0, column=2,padx=10,pady=10,sticky=W)

        studenName_entry=ttk.Entry(class_employee_frame , textvariable=self.var_emp_name,width=20, font=("times new roman", 13, "bold"))
        studenName_entry.grid (row=0, column=3, padx=10, pady=5, sticky=W)


        # Gender
        gender_label=Label(class_employee_frame, text="Gender :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        gender_label.grid(row=1, column=0,padx=10,pady=10,sticky=W)

        gender_combo=ttk.Combobox(class_employee_frame , textvariable=self.var_gender,width=18, font=("times new roman", 13, "bold"),state="readonly")
        gender_combo["values"]=("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid (row=1, column=1, padx=10, pady=5, sticky=W)

        
        # DOB
        DOB_label=Label(class_employee_frame, text="DOB :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        DOB_label.grid(row=1, column=2,padx=10,pady=10,sticky=W)

        DOB_entry=ttk.Entry(class_employee_frame , textvariable=self.var_dob,width=20, font=("times new roman", 13, "bold"))
        DOB_entry.grid (row=1, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label=Label(class_employee_frame, text="Email :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        email_label.grid(row=2, column=0,padx=10,pady=10,sticky=W)

        email_entry=ttk.Entry(class_employee_frame , textvariable=self.var_email , width=20, font=("times new roman", 13, "bold"))
        email_entry.grid (row=2, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_no_label=Label(class_employee_frame, text="Phone No :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        phone_no_label.grid(row=2, column=2,padx=10,pady=10,sticky=W)

        phone_no_entry=ttk.Entry(class_employee_frame , textvariable=self.var_phone,width=20, font=("times new roman", 13, "bold"))
        phone_no_entry.grid (row=2, column=3, padx=10, pady=5, sticky=W)
       
       
        
        # Proof Type
        proof_type_label=Label(class_employee_frame, text="Proof Type :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        proof_type_label.grid(row=3, column=0,padx=10,pady=10,sticky=W)

        proof_type_combo=ttk.Combobox(class_employee_frame , textvariable=self.var_proof_type,width=18, font=("times new roman", 13, "bold"),state="readonly")
        proof_type_combo["values"]=("Select Proof", "Aadhar Card", "PAN Card")
        proof_type_combo.current(0)
        proof_type_combo.grid (row=3, column=1, padx=10, pady=5, sticky=W)

        # Proof No
        proof_no_label=Label(class_employee_frame, text="Proof No :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        proof_no_label.grid(row=3, column=2,padx=10,pady=10,sticky=W)

        proof_no_entry=ttk.Entry(class_employee_frame , textvariable=self.var_proof_no,width=20, font=("times new roman", 13, "bold"))
        proof_no_entry.grid (row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        Address_label=Label(class_employee_frame, text="Address :", font=("times new roman", 13, "bold"),bg="white",fg="black")
        Address_label.grid(row=4, column=0,padx=10,pady=10,sticky=W)

        Address_entry=ttk.Entry(class_employee_frame , textvariable=self.var_address,width=20, font=("times new roman", 13, "bold"))
        Address_entry.grid (row=4, column=1, padx=10, pady=5, sticky=W)


         # radio Buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_employee_frame , text="Take Photo Sample",variable=self.var_radio1 ,  value="Yes")
        radionbtn1.place(x=420,y=222,height=17)
        
        
        radionbtn2=ttk.Radiobutton(class_employee_frame, text="No Photo Sample" , variable=self.var_radio1 , value="No")
        radionbtn2.place(x=570,y=222,height=17)

        # bbuttons frame

        save_btn=Button (Left_frame , command=self.add_data , text="Save",width=17, font=("times new roman", 13, "bold"), bg="green", fg="white")
        save_btn.place(x=8,y=486,width=181.25,height=33)

        update_btn=Button (Left_frame , command=self.update_data , text="Update",width=18, font=("times new roman", 13, "bold"), bg="green", fg="white")
        update_btn.place(x=189.25,y=486,width=181.5,height=33)

        delete_btn=Button (Left_frame , command=self.delete_data , text="Delete",width=17, font=("times new roman", 13, "bold"), bg="green", fg="white")
        delete_btn.place(x=370.5,y=486,width=181.25,height=33)

        reset_btn=Button (Left_frame , command=self.reset_data , text="Reset",width=17, font=("times new roman", 13, "bold"), bg="green", fg="white")
        reset_btn.place(x=551.75,y=486,width=181.25,height=33)


        # bbuttons frame1
      
        take_photo_btn=Button (Left_frame , command=self.generate_dataset , text="Take Photo Sample",width=36, font=("times new roman", 13, "bold"), bg="green", fg="white")
        take_photo_btn.place(x=8,y=519,width=362.5,height=33)

        update_photo_btn=Button (Left_frame, text="Update Photo Sample",width=36, font=("times new roman", 13, "bold"), bg="green", fg="white")
        update_photo_btn.place(x=370.5,y=519,width=362,height=33)



        # Right label frame
        Right_frame=LabelFrame(bg_img, bd=15,bg="cyan", relief=RIDGE, font=("times new roman",12,"bold"))
        Right_frame.place(x=815, y=60,width=675,height=590)

        dep_label_2=Label(Right_frame, text="Employee Details", font=("times new roman", 20, "bold"),bg="cyan",fg="black")
        dep_label_2.place(x=220,y=0,width=250,height=50)

        #============================ Search System ================================

        # search_frame=LabelFrame(Right_frame, bd=10,bg="white",fg="black", relief=RIDGE, text=" Search System ", font=("times new roman",15,"bold"))
        # search_frame.place(x=8, y=55,width=630,height=85)

        # search_label=Label(search_frame, text="Search By : ", font=("times new roman", 12, "bold"),bg="white",fg="black")
        # search_label.place(x=8,y=12,width=90,height=25)

        # search_combo=ttk.Combobox(search_frame, font=("times new roman", 12, "bold"),state="readonly",width=15)
        # search_combo["values"]=("Select", "Proof_No", "Phone_No")
        # search_combo.current(0)
        # search_combo.place(x=110,y=12,width=120,height=25)

        # search_entry=ttk.Entry(search_frame,width=15, font=("times new roman", 13, "bold"))
        # search_entry.place(x=240,y=12,width=150,height=25)

        # search_btn=Button (search_frame, text="Search",width=10, font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        # search_btn.place(x=410,y=12,width=90,height=25)

        # showAll_btn=Button (search_frame, text="Show All",width=10, font=("times new roman", 12, "bold"), bg="darkblue", fg="white")
        # showAll_btn.place(x=510,y=12,width=90,height=25)

        #============================ Table Frame ================================

        table_frame=Frame(Right_frame, bd=10,bg="darkblue", relief=RIDGE)
        table_frame.place(x=8, y=50,width=630,height=500)

        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)
        
        self.employee_table=ttk. Treeview (table_frame, column=("id", "name","dep","dep_id", "date","proof_type", "proof_no", "gender", "dob", "email" , "phone","address", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)


        self.employee_table.heading("id",text="EmployeeId")
        self.employee_table.heading("name", text="Name")
        self.employee_table.heading ("dep", text="Department")
        self.employee_table.heading("dep_id", text="dep_id")
        self.employee_table.heading("date", text="date")
        self.employee_table.heading("proof_type", text="proof_type")
        self.employee_table.heading("proof_no", text="proof_no")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading ("dob", text="DOB")
        self.employee_table.heading ("email", text="Email")
        self.employee_table.heading("phone", text="Phone")
        self.employee_table.heading("address", text="Address")
        self.employee_table.heading("photo", text="PhotoSampleStatus")
        self.employee_table["show"]="headings"

       
        self.employee_table.column("id",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("dep",width=100)
        self.employee_table.column("dep_id",width=100)
        self.employee_table.column ("date",width=100)
        self.employee_table.column("proof_type",width=100)
        self.employee_table.column("proof_no",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column ("dob",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("photo",width=150)
        
        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #==================================Function Declaration======================================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_dep_id.get()=="Select ID" or self.var_date.get()=="Select Date" or self.var_emp_id.get()=="" or self.var_emp_name.get()=="" or self.var_proof_type.get()=="Select Proof" or self.var_proof_no.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_radio1.get()=="" :
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="empl_face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into employee values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    
                                                                                                self.var_emp_id.get(),
                                                                                                self.var_emp_name.get(),
                                                                                                self.var_dep.get(),
                                                                                                self.var_dep_id.get(),
                                                                                                self.var_date.get(),
                                                                                                self.var_proof_type.get(),
                                                                                                self.var_proof_no.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_radio1.get()

                                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee details has been added Successfully!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #==================================Fetch Data======================================
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="empl_face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from employee")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #===============================Get Cursor=========================================

    def get_cursor(self,event=""):
        cursor_focus=self.employee_table.focus()
        content=self.employee_table.item(cursor_focus)
        data=content["values"]

        
        self.var_emp_id.set(data[0]),
        self.var_emp_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_dep_id.set(data[3]),
        self.var_date.set(data[4]),
        self.var_proof_type.set(data[5]),
        self.var_proof_no.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])


    #==================================Update Function=======================================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_dep_id.get()=="Select ID" or self.var_date.get()=="Select Date" or self.var_emp_id.get()=="" or self.var_emp_name.get()=="" or self.var_proof_type.get()=="Select Proof" or self.var_proof_no.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_radio1.get()=="" :
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Employee details?",parent=self.root)

                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="empl_face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update employee set  Name=%s , Dep=%s , dep_id=%s , date=%s ,  proof_type=%s , proof_no=%s , Gender=%s , Dob=%s , Email=%s , Phone=%s , Address=%s , PhotoSample=%s where Employee_id=%s",(
                                                                                                              
                                                                                                                                                                                
                                                                                                                                                                                self.var_emp_name.get(),
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_dep_id.get(),
                                                                                                                                                                                self.var_date.get(),
                                                                                                                                                                                self.var_proof_type.get(),
                                                                                                                                                                                self.var_proof_no.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_emp_id.get()

                                                                                                                                                                                                                ))
                    messagebox.showinfo("Success","Employee datails update Successfully Completed !",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()



                else:
                    if not update:
                        return

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #==================================Delete Function=======================================

    def delete_data(self):
        if self.var_emp_id.get()=="":
            messagebox.showerror("Error","Employee ID must be required!",parent=self.root)

        else:
            try:
                delete=messagebox.askyesno("Employee Data Delete Page","Do you want to delete this employee datails?",parent=self.root)

                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="empl_face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from employee where Employee_id=%s"
                    val=(self.var_emp_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully Deleted Employee Details!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    #==================================Reset Function=======================================

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_dep_id.set("Select ID")
        self.var_date.set("Select Date")
        self.var_emp_id.set("")
        self.var_emp_name.set("")
        self.var_proof_type.set("Select Proof")
        self.var_proof_no.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")


    #======================= Generate Dta set OR Take Photo Samples =========================

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_dep_id.get()=="Select ID" or self.var_date.get()=="Select Date"  or self.var_emp_id.get()=="" or self.var_emp_name.get()=="" or self.var_proof_type.get()=="Select Proof" or self.var_proof_no.get()=="" or self.var_gender.get()=="Select Gender" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_radio1.get()=="" :
            messagebox.showerror("Error","All Fields Are Required!",parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456", database="empl_face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee")
                myresult=my_cursor.fetchall()
                print(myresult)
               
                my_cursor.execute("update employee set  Name=%s , Dep=%s , dep_id=%s , date=%s , proof_type=%s , proof_no=%s , Gender=%s , Dob=%s , Email=%s , Phone=%s , Address=%s , PhotoSample=%s where Employee_id=%s",(
                                                                                                              
                                                                                                                                                                                
                                                                                                                                                                                self.var_emp_name.get(),
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_dep_id.get(),
                                                                                                                                                                                self.var_date.get(),
                                                                                                                                                                                self.var_proof_type.get(),
                                                                                                                                                                                self.var_proof_no.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.var_emp_id.get()

                                                                                                                                                                                                                ))

                id=self.var_emp_id.get()


                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                #============================== Load Predefine Data On Face frontals from OpenCV ===============================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor = 1.3
                    # Minimum neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0

                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+ str(id) +"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            



if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()