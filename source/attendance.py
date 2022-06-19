from tkinter import*
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
from cv2 import FONT_HERSHEY_COMPLEX
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recogniton System")


        #===================== Variables ==========================

        self.var_atten_id=StringVar()
        self.var_atten_proof_no=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        # bg Image
        img3=Image.open(r"college_images\wp2551980.jpg")
        img3=img3.resize((1540,900), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
 
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1540,height=900)


        # Title Frame
        main_frame=Frame(self.root,bd=2,bg="green")
        main_frame.place(x=0, y=30,width=1540,height=55)

        title_lbl=Label(main_frame,text="ATTENDANCE  MANAGEMENT  SYSTEM",font=("times new roman", 35, "bold"),bg="blue",fg="white")
        title_lbl.place(x=0, y=0,width=1530, height=50)

        # Left label frame
        Left_frame=LabelFrame(bg_img, bd=20,bg="cyan", relief=RIDGE, font=("times new roman",12,"bold"))
        Left_frame.place(x=40, y=180,width=710,height=515)

        dep_label_1=Label(Left_frame, text="Employee Details", font=("times new roman", 25, "bold"),bg="cyan",fg="black")
        dep_label_1.place(x=200,y=0,width=300,height=50)

        # Left Inside Frame 
        left_inside_frame=Frame(Left_frame,bd=10,relief=RIDGE,bg="darkblue")
        left_inside_frame.place(x=15, y=60,width=640,height=400)


        # Lables and Entry
        # Attendance ID
        attendanceID_label=Label(left_inside_frame, text="Employee ID :", font=("times new roman", 13, "bold"),bg="darkblue",fg="white")
        attendanceID_label.grid(row=0, column=0, padx=10,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame , width=15,textvariable=self.var_atten_id, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid (row=0, column=1, padx=10, pady=30, sticky=W)

         #Department
        deplabel=Label(left_inside_frame, text="Department :",bg="darkblue", font="comicsansns 11 bold",fg="white")
        deplabel.grid(row=0,column=2,padx=10,sticky=W)

        atten_dep=ttk. Entry(left_inside_frame, width=15, textvariable=self.var_atten_dep, font="comicsansns 11 bold")
        atten_dep.grid(row=0, column=3, padx=10, pady=30, sticky=W)

       
        
        #Name
        namelabel=Label(left_inside_frame, text="Employee Name :", bg="darkblue", font="comicsansns 11 bold",fg="white")
        namelabel.grid(row=1,column=0,padx=10,sticky=W)

        atten_name=ttk. Entry(left_inside_frame, width=15,textvariable=self.var_atten_name, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, padx=10, pady=30, sticky=W)

         # Phone No
        proof_no_Label=Label(left_inside_frame, text="Phone No :", bg="darkblue", font="comicsansns 11 bold",fg="white")
        proof_no_Label.grid(row=1,column=2,padx=10,sticky=W)

        atten_proof_no=ttk. Entry(left_inside_frame, width=15,textvariable=self.var_atten_proof_no, font="comicsansns 11 bold")
        atten_proof_no.grid(row=1,column=3, padx=10, pady=30, sticky=W)
       
        #time
        timelabel=Label(left_inside_frame, text="Time :",bg="darkblue", font="comicsansns 11 bold",fg="white")
        timelabel.grid(row=2, column=0,padx=10,sticky=W)

        atten_time=ttk. Entry(left_inside_frame, width=15,textvariable=self.var_atten_time, font="comicsansns 11 bold")
        atten_time.grid(row=2,column=1, padx=10, pady=30, sticky=W)

        #Date
        datelabel=Label(left_inside_frame, text="Date :",bg="darkblue",font="comicsansns 11 bold",fg="white")
        datelabel.grid(row=2,column=2,padx=10,sticky=W)

        atten_date=ttk. Entry(left_inside_frame,width=15,textvariable=self.var_atten_date, font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, padx=10, pady=30, sticky=W)

        #attendance
        attendancelabel=Label(left_inside_frame, text="Attendance Status :", bg="darkblue", font="comicsansns 11 bold",fg="white")
        attendancelabel.place(x=70,y=268,width=300,height=35)

        self.atten_status=ttk.Combobox (left_inside_frame,width=15,textvariable=self.var_atten_attendance, font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present", "Absent")
        self.atten_status.grid(row=3, column=2, padx=10, pady=20, sticky=W)
        self.atten_status.current(0)

        # bbuttons frame
        
        update_btn=Button (left_inside_frame , text="Update",width=17, font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        update_btn.place(x=90,y=335)

        reset_btn=Button (left_inside_frame , text="Reset",command=self.reset_data , width=17, font=("times new roman", 13, "bold"), bg="darkgreen", fg="white")
        reset_btn.place(x=350,y=335)


        # Right label frame
        Right_frame=LabelFrame(bg_img, bd=20,bg="cyan", relief=RIDGE, font=("times new roman",12,"bold"))
        Right_frame.place(x=780, y=180,width=710,height=515)

        dep_label_1=Label(Right_frame, text="Attendance Details", font=("times new roman", 25, "bold"),bg="cyan",fg="black")
        dep_label_1.place(x=200,y=0,width=300,height=50)

        table_frame=Frame(Right_frame, bd=10,bg="darkblue", relief=RIDGE)
        table_frame.place(x=10, y=60,width=660,height=385)

        import_btn=Button (Right_frame , text="Import csv",command=self.importCsv,width=17, font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        import_btn.place(x=150, y=450,width=190,height=33)

        export_btn=Button (Right_frame , text="Export csv",command=self.exportCsv,width=18, font=("times new roman", 13, "bold"), bg="darkblue", fg="white")
        export_btn.place(x=370, y=450,width=190,height=33)

        #====================== Scroll Bar Table ==========================

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id", "proof_no" , "name", "Department", "time" , "date" , "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("proof_no",text="proof No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("proof_no",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #======================= Fetch Data =======================

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())

        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)


    #==== Import csv ======
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    #==== Export csv ======
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}", parent=self.root)


    #========================= Get Cursor ================================

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_proof_no.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    #========================= Reset Data ================================

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_proof_no.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance. set("")


if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()