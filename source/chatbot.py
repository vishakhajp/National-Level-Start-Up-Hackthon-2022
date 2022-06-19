from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from numpy import right_shift#pip install pillow




class ChatBot:
    def __init__(self, root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind("<Return>",self.enter_func)


        main_frame=Frame(self.root, bd=4, bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open('chat.jpg')
        img_chat=img_chat.resize((150,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage (img_chat)

        Title_label=Label(main_frame, bd=3, relief=RAISED, anchor='nw', width=730,compound=LEFT, image=self.photoimg, text='CHAT ME', font=('arial',30,'bold'),fg="green",bg="white")
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar (main_frame, orient=VERTICAL)
        self.text=Text(main_frame,width=65, height=20,bd=3,relief=RAISED, font=('arial',14), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4, bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame, text="Type Something", font=('arial',14, 'bold'),fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)


        self.entry=StringVar()
        self.entry1=ttk. Entry(btn_frame, width=40,textvariable=self.entry, font=('Times new roman',16, 'bold'))
        self.entry1.grid(row=0, column=1, padx=5, sticky=W)

        self.send=Button(btn_frame, text="Send>>",command=self.send, font=('arial',13,'bold'), width=8, bg='green',fg="white")
        self.send.grid(row=0,column=2, padx=5, sticky=W)

        self.clare=Button(btn_frame, text="Clear Data",command=self.clear, font=('arial',15,'bold'), width=8, bg='cyan', fg='black')
        self.clare.grid(row=1,column=1,padx=160,pady=10, sticky=W)

        self.msg=""
        self.label_11=Label(btn_frame, text=self.msg, font=('arial',14,'bold'),fg='red', bg='white')
        self.label_11.place(x=0,y=550)

    #========================= Function Declaration =======================

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')


    def clear(self):
        self.text.delete('1.0', END)
        self.entry.set('')



    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END, '\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg, fg='red')

        else:
            self.msg=""
            self.label_11.config(text=self.msg, fg='red')

        if (self.entry.get()=='hello'):
            self.text.insert(END, '\n\n'+'Bot: Hi')

        elif (self.entry.get()=="hi"):
            self.text.insert(END,"\n\n"+"Bot: Hello")

        elif (self.entry.get()=="How are you?"):
            self.text.insert(END,"\n\n"+"Bot: fine and you")

        elif (self.entry.get()=="Fantastic"):
            self.text.insert(END,"\n\n"+"Bot: Nice To Hear")

        elif (self.entry.get()=="Who created you?"):
            self.text.insert(END, "\n\n"+"Bot: Vishakha did using python")
            
        elif (self.entry.get()=="What is your name?"):
            self.text.insert(END,"\n\n"+"Bot: My name is Mr. Hacker")
        
        elif (self.entry.get()=="Can you speak Marathi"):
            self.text.insert(END,"\n\n"+"Bot: I'm still learning it..")

        elif (self.entry.get()=="What is machine learning?"):
            self.text.insert(END, "\n\n"+"Bot: Machine learning isabranch\nof artificial intelligence (AI) focused\non building applications that learn\nfrom data and improve their accuracy\nover time without being programmed\nto do so.")

        elif (self.entry.get()=="How does face recognition work?"):
            self.text.insert(END, "\n\n"+"Bot: Facial recognition isaway of\nrecognizingahuman face through\ntechnology. A facial recognition\nsystem uses biometrics to map\nfacial features fromaphotograph\nor video. It compares the information\nwith a database of known faces to find\na match.")

        elif (self.entry.get()=="How does facial recognition work step by step?"):
            self.text.insert(END,"\n\n"+"Bot: Step 1: Face detection. The camera\ndetects and locates the image of a face, \neither alone or inacrowd. .. \nStep 2: Face analysis. Next, an image of\n the face is captured and analyzed. ...\nStep 3: Conversation.")

        elif (self.entry.get()=="How many countries use facial recognition?"):
                self.text.insert(END, "\n\n"+"Bot: In Use 98\nApproved, but not implemented 12\nConsidering facial recognition technology 13\nNo evidence of use 68")

        elif (self.entry.get()=="What is python programming?"):
                self.text.insert(END, "\n\n"+"Bot:Python isageneral purpose\nand high level programming language.\nYou can use Python for developing\ndesktop GUI applications, websites\nand web applications. Also, Python, \nasahigh level programming language.")

        elif (self.entry.get()=="What is chatbot?"):
            self.text.insert(END,"\n\n"+"Bot:A chatbot isacomputer\nprogram that's designed to\nsimulate human conversation.")

        elif (self.entry.get()=="bye"):
            self.text.insert(END, "\n\n"+"Bot: Thank You For Chatting")

        else:
            self.text.insert(END, "\n\n"+"Bot: Sorry I dindn't get it")







if __name__=="__main__":
     root=Tk()
     obj=ChatBot(root)
     root.mainloop()