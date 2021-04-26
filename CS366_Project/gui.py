import tkinter as tk
from tkinter import *
from tkinter import ttk
from DataClasses import MedicalTests 
#from DataClasses import PatientMedicalHistory
from DataClasses import Patient
from DataClasses import Doctor
from DataClasses import Pharmacist
from DataClasses import *
from Database import *
#from tkinter import messageboxfrom PIL import ImageTk,Image #PIL -> Pillow

root = Tk()
root.title("Valitado")
root.minsize(width=400,height=400)
root.geometry("700x700")
#root.mainloop()



headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to \n Valitudo Hospital", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Doctor",bg='black', fg='red', command=Doctor)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Patient",bg='black', fg='red', command=Patient)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="Pharmacist",bg='black', fg='red', command=Pharmacist)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
"""btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)"""


root.mainloop()


















