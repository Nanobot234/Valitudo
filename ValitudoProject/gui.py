import tkinter as tk
import tkinter.ttk as ttk
from  Database import Database
from DataClasses import *
import PyQt5



import tkinter as tk


#controller
class SeaofBTCapp(tk.Tk):

    def __init__(self,*args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

     

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo,SearchForPatient):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0,column=0,sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)


        #label = tk.Label(self, text="Start Page", font=LARGE_FONT)
       
        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        #label.(pady=10,padx=10)
        
        self.database = Database()
        self.controller = controller
        self.label1 = tk.Label(self,text='Please enter your id').pack(pady=20)

        self.login_input = tk.StringVar()
        entry1 = tk.Entry(self,textvariable=self.login_input)
        
        entry1.pack()
        self.errorlabel = tk.Label(self)


        self.button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))

        self.button1.pack()

        self.button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        self.button2.pack()
        
        self.loginButton = tk.Button(self,text='Log In',command=self.validate)
        self.loginButton.pack()

    

    def validate(self):
        doctorInfo = self.database.findDoctorWithSpecificID((self.login_input.get()))
        if (len(doctorInfo) == 0):
                    self.errorlabel.configure(text="Invalid login please check again, or register in the database")
                    self.errorlabel.pack()
        else:
            self.loginButton.configure(command=lambda:self.controller.show_frame(PageTwo))
            
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        

        button1 = tk.Button(self, text="Search for Patient",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side="left")


        button2 = tk.Button(self, text="Page One",
                            command=self.printValue)
        button2.pack()

    def printValue(self):
        print(self.value)

class SearchForPatient(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

db = Database()
doctor = Doctor(2345,"Nana","Bonsu",345,34,"male","2350 Ryer Avenue","cardio")







app = SeaofBTCapp()
app.geometry("700x700")
app.mainloop()

