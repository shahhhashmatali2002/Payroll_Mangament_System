# ......................| Import Library |.........................
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkcalendar import Calendar
import pyodbc
# --------|                                      |--------------
#             Querry for Database Exist or not
# --------|                                      |--------------
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-SK0J9LF;"
    "Trusted_Connection=yes;"
)
conn.autocommit = True

if conn is not None:
    conn.autocommit = True
else:
    print("Connect not Successfully:")

# Asking user to enter database name he wants to check
# database_name = input('Enter database name to check exist or not: ')
database_name = "Payroll_Management"
cur = conn.cursor()
cur.execute("SELECT name FROM master.dbo.sysdatabases where name=?;", (database_name,))
data = cur.fetchall()

print(data)

# Printing if database exists or not
if not data:
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-SK0J9LF;"
        "Trusted_Connection=yes;"
    )
    conn.autocommit = True

    cursor = conn.cursor()

    cursor.execute(
        '''
        Create database Payroll_Management
        '''
    )

    conn.commit()
    print("Database Successfully Create")
else:
    print("'{}' Database already exists".format(database_name))

#--| import Module |--
from abc import ABC, abstractmethod
from Dashboard import *


class FirstWindow1(ABC):
    @abstractmethod
    def FW(self):
        pass

class FirstWindow(FirstWindow1):
    def FW(self):
        # __________| login window Start  |_______
        # self.first_window = Tk
        self.first_window = Tk()
        self.first_window.title("Login ID")
        self.first_window.geometry('1366x768')
        self.first_window.configure(background="darkblue")
        # ___| first_window resizing disable |____
        # super().__init__(first_window)
        self.first_window.resizable(0, 0)
        # title = Label(self.first_window,text='Login Here',font=("times new roman", 10,"bold"),bg="gray",fg="black",width=120,height=2 ).place(x=0,y=0)

        # _________| Frame1 in login window Start |________
        self.bg1 = ImageTk.PhotoImage(file="C:/images/wall.jpg"
                                 )
        self.frame1 = Frame(self.first_window, bg='tomato').place(x=500, y=100, width=800, height=500)
        self.Bg1 = Label(self.frame1, image=self.bg1).place(x=500, y=100, width=800, height=500)
        # _________| Frame1 in login window End |________

        # _______| image in Frame1 in login window Start |__________
        self.log1 = ImageTk.PhotoImage(file="C:/images/payroll1.jpg")
        self.log = Label(self.frame1, image=self.log1).place(x=152, y=120, width=451, height=450)
        # _______| image in Frame1 in login window End |__________

        # _______| title in frame1 in login window Start |_________
        self.title1 = Label(self.frame1, text="Payroll Management System", width='46', font=("times new roman", 20),
                       fg="white", bg="black").place(x=604, y=120)
        # _______| title in frame1 in login window End |_________

        # ..........................| variable for catch data from entry box in login window  Start |..............................
        self.login = StringVar()
        self.password = StringVar()
        # ..........................| variable for catch data from entry box in login window End |..............................

        # ................................| labels and entrys in login window Start |..........................................
        self.lbl = Label(self.first_window, text="User Name", width='10', font=("times new roman", 15), fg='white',
                    bg="black").place(x=650, y=200)
        self.entry = Entry(self.first_window, textvariable=self.login, width=35, ).place(x=780, y=200, height=29)
        self.lbl1 = Label(self.first_window, text="User Pasword", width='10', font=("times new roman", 15), fg='white',
                     bg="black").place(x=650, y=300)
        self.entry1 = Entry(self.first_window, textvariable=self.password, width=35, show="*").place(x=780, y=300, height=29)

        self.bg2 = ImageTk.PhotoImage(file="C:/images/bgimage1.jpg")

        self.btn = Button(self.frame1, image=self.bg2, font=("times new roman", 15), activebackground="red",command=self.loginnow).place(
            x=680, y=370)

        self.first_window.mainloop()

    def loginnow(self):
        if self.login.get() == "" and self.password.get() == "":
            messagebox.showerror("Alert", "Please Enter Username and Password!")

        elif self.login.get() != "hashmat ali" and self.password.get() != "0987":
            messagebox.showerror("Error","Invalid UserName or Password!")

        elif self.login.get() == "hashmat ali" and self.password.get() == "0987":
            messagebox.showinfo("Info", "Successfully Login")
            self.first_window.destroy()
            print(f"User Name: {self.login.get()}")
            print(f"User Password: {self.password.get()}")

            dashboard_Window = Tk()
            obj = Dashboard_Window(dashboard_Window)
            dashboard_Window.mainloop()



mainobj = FirstWindow()
mainobj.FW()

