from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkcalendar import Calendar
import pyodbc
# from main import *
# --------|                                      |--------------
#             Querry for Table Exist or not
# --------|                                      |--------------
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-SK0J9LF;"
    "Database=Payroll_Management;"
    "Trusted_Connection=yes;"
)
conn.autocommit = True

# Asking user to enter database name he wants to check
# database_name = input('Enter database name to check exist or not: ')
table_name = "Hour_Base_Employee_Salary"
cur = conn.cursor()
cur.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?;", (table_name,))
data = cur.fetchall()

print(type(data))

# Printing if database exists or not
if not data:
    conn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=DESKTOP-SK0J9LF;"
        "Database=Payroll_Management;"
        "Trusted_Connection=yes;"
    )
    conn.autocommit = True

    cursor = conn.cursor()
    cursor.execute(
        '''
        Create table Hour_Base_Employee_Salary(
                Salary_ID int Identity(1,1) Not Null,
                Employee_ID int Not Null,
                Image_Path nvarchar(255) Not Null,
                Date Date Not Null,
                Rate int Not Null,
                Hour int Not Null,
                OverTime float Not Null,
                GrossPay float Not Null,
                Tax int Not Null,
                NetPay float Not Null,
                Constraint PK_Hour_Base_Employee_Salary Primary Key (Salary_ID),
                FOREIGN KEY (Employee_ID) REFERENCES HBES_EI(Employee_ID)
	                )
        '''
    )
    print(" '{}' table Successfully Create in Payroll_Management Database".format(table_name))
else:
    print(" '{}' table Exist in Payroll_Managemment Database".format(table_name))


class HBES():
    def __init__(self, root):
        self.root = root
        self.root.title('Monthly Base Employee Salary')
        self.root.geometry('1360x768+0+0')
        self.root.resizable(0, 0)
        title = Label(self.root, text="HOUR BASE EMPLOYEE SALARY", bd=4, font=("times new roman", 40), bg="navy",
                      fg="oldlace", relief=GROOVE, justify=CENTER)
        title.pack(side=TOP, fill=X)
        # ________| Manage Frame |___________
        self.Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#2e5cbe")
        self.Manage_Frame.place(x=20, y=100, width=500, height=620)

        # ______| Function for Entry placeholder removing |__________
        def click1(*args):
            if self.EID['state'] != DISABLED:
                messagebox.showinfo("Information",
                                    "Please Don't try to insert\nBecause Employee ID Fetch from Treeview")
                return "break"

        def click2(*args):
            if self.EN['state'] != DISABLED:
                messagebox.showinfo("Information",
                                    "Please Don't try to insert\nBecause Employee Name Fetch from Treeview")
                return "break"

        def click3(event):
            self.ER.focus()
            self.ER.delete(0, END)

        def click4(*args):
            self.EOT.focus()
            self.EOT.delete(0, END)

        def click6(*args):
            self.EIT.focus()
            if self.EIT.get() == 'Employee Tax':
                self.EIT.focus()
                self.EIT.delete(0, 'end')

        def click8(*args):
            messagebox.showinfo("Information", "Click on Calculate Button Value Auto Set")
            return "break"

        def click9(*args):
            messagebox.showinfo("Information", "Click on Calculate Button Value Auto Set")
            return "break"


        def click10(*args):
            self.EH.focus()
            self.EH.delete(0, END)

            # ________| leave Function |_________

        def leave(*args):
            self.Manage_Frame.focus()
            if self.Employee_id.get() == "":
                self.EID.insert(0, 'Employee ID')
                self.Manage_Frame.focus()
            elif self.Employee_name.get() == "":
                self.EN.insert(0, 'Employee Name')
                self.Manage_Frame.focus()
            elif self.ER.get() == "":
                self.ER.insert(0, 'Employee Rate')
                self.Manage_Frame.focus()
            elif self.EH.get() == "":
                self.EH.insert(0, 'Employee Hour')
                self.Manage_Frame.focus()
            elif self.EOT.get() == "":
                self.EOT.insert(0, 0)
                self.Manage_Frame.focus()

            # _-_-) Data Enter in Employee Gross Pay (_-_
            elif self.EGP.get() == "":
                self.EGP.insert(0, 'Employee Gross Pay')
                self.Manage_Frame.focus()
            elif self.EIT.get() == "":
                self.EIT.insert(0, 'Employee Tax')
                self.Manage_Frame.focus()
            elif self.ENP.get() == "":
                self.ENP.insert(0, 'Employee Net Pay')
                self.Manage_Frame.focus()

        # call function when we  entry box
        self.Date = StringVar()
        self.Employee_id = StringVar()
        self.Employee_name = StringVar()
        self.Employee_Rate = IntVar()
        self.Employee_Hour = IntVar()
        self.Employee_Overtime = float()
        self.Employee_Gross_Pay = float
        self.Employee_Income_Tax = IntVar()
        self.Employee_Company_Tax = StringVar()
        self.Employee_Net_Pay = float
        self.Employee_img = StringVar()

        # #________| Date Pciker |________
        Label(self.Manage_Frame, text="Date: ", bg="#2e5cbe", fg="white", font=("times new roman", 20, "bold")).place(
            x=10, y=10)
        cal = DateEntry(self.Manage_Frame, textvariable=self.Date, width=10, day=1, month=1, year=2021,
                        background='darkblue', foreground='white', borderwidth=2, font=("times new roman", 15, "bold"),
                        state='readonly')
        cal.place(x=100, y=20)

        self.go_btn = Button(self.Manage_Frame, text='GO', width=10, font=("times new roman", 10, "bold"),
                             relief=GROOVE,
                             bd=4, bg='teal', fg='oldlace', command=self.go)
        self.go_btn.place(x=250, y=18)
        # self.Manage_Frame.focus()

        # ______| Upload Image Frame |_______

        self.upload_image = Frame(self.Manage_Frame, width=192, height=192).place(x=260, y=60)

        def NE_EI(*args):
            messagebox.showinfo("Information",
                                "Please dont't try to Insert Image Path\nBecause Image Path Fetch from Database!")
            return "break"

        self.Employee_Image = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                                    textvariable=self.Employee_img)
        self.Employee_Image.place(x=250, y=270)
        self.Employee_Image.insert(0, 'Employee Image')
        self.Employee_Image.bind("<Button-1>", NE_EI)
        self.Employee_Image['state'] = DISABLED

        # ________| Entry Box Start |_______
        # _________| EID = Employee ID (Entry Box) |_________
        self.EID = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15), textvariable=self.Employee_id)

        # Add text in Entry box
        self.EID.insert(0, 'Employee ID')
        self.EID.place(x=20, y=90)

        # Use bind method
        self.EID.bind("<Button-1>", click1)
        self.EID.bind("<Leave>", leave)
        self.EID['state'] = DISABLED

        # ________| EN = Employee Name (Entry Box) |________
        self.EN = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                        textvariable=self.Employee_name)

        # Add text in Entry box
        self.EN.insert(0, 'Employee Name')
        self.EN.place(x=20, y=150)

        # Use bind method
        self.EN.bind("<Button-1>", click2)
        self.EN.bind("<Leave>", leave)
        self.EN['state'] = DISABLED

        # __________| ER = Employee Rate (Entry Box) |_____________

        # _-_-_-_-_| Function not allo |_-_-_-_-_-_
        def only_allow(event):
            char = event.char.lower()
            if (event.state & 3) >> 2:
                return None

            if char.isprintable() and (not event.char.isdigit()):
                messagebox.showerror("Error", "String Not Allow\nPlease Enter Number")
                return "break"
            elif len(self.ER.get()) > 2:
                self.ER.focus()
                # self.NE_nic.focus()
                return "break"

        self.ER = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                        textvariable=self.Employee_Rate)
        # Add text in Entry box
        self.ER.delete(0, END)
        self.ER.insert(0, 'Employee Rate')
        self.ER.place(x=20, y=210)

        # Use bind method
        self.ER.bind("<Button-1>", click3)
        self.ER.bind("<Leave>", leave)
        self.ER.bind("<Key>", only_allow)
        self.ER['state'] = DISABLED

        # __________| EH = Employee Hour (Entry Box) |____________

        # _-_-_-_-_| Function not allo |_-_-_-_-_-_
        def only_allow_EH(event):
            char = event.char.lower()
            if (event.state & 3) >> 2:
                return None

            if char.isprintable() and (not event.char.isdigit()):
                messagebox.showerror("Error", "String Not Allow\nPlease Enter Number")
                return "break"
            elif len(self.EH.get()) > 0:
                self.EH.focus()
                # self.NE_nic.focus()
                return "break"

        self.EH = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                        textvariable=self.Employee_Hour)
        self.EH.delete(0, END)
        self.EH.insert(0, 'Employee Hour')
        self.EH.place(x=20, y=270)
        # use Bind method
        self.EH.bind("<Button-1>", click10)
        self.EH.bind("<Leave>", leave)
        self.EH.bind("<Key>", only_allow_EH)
        self.EH['state'] = DISABLED

        # __________| EOT = Employee Over Time (Entry Box) |____________

        def not_allow_EOT(event):
            char = event.char.lower()

            if (event.state & 3) >> 2:
                return None

            if char.isprintable() and (not event.char.isdigit()):
                messagebox.showerror("Error", "String Not Allow\nPlease Enter Number")
                return "break"
            elif len(self.EOT.get()) > 0:
                self.EOT.focus()
                return "break"

        self.EOT = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                         textvariable=self.Employee_Overtime)
        # Add text in Entry box
        self.EOT.delete(0, END)
        self.EOT.insert(0, 'Employee Over Time')
        self.EOT.place(x=20, y=330)

        # Use bind method
        self.EOT.bind("<Button-1>", click4)
        self.EOT.bind("<Leave>", leave)
        self.EOT.bind("<Key>", not_allow_EOT)
        self.EOT['state'] = DISABLED
        # ___________| EIT = Employee Income Tax |___________
        self.EIT = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                         textvariable=self.Employee_Income_Tax)
        # Add text in Entry box
        self.EIT.delete(0, END)
        self.EIT.insert(0, 'Employee Tax')
        self.EIT.place(x=20, y=390)

        # Use bind method
        self.EIT.bind("<Button-1>", click6)
        self.EIT.bind("<Leave>", leave)
        self.EIT['state'] = DISABLED

        # ___________| ENP = Employee Net Pay |___________
        self.ENP = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                         textvariable=self.Employee_Net_Pay)
        # Add text in Entry box
        self.ENP.insert(0, 'Employee Net Pay')
        self.ENP.place(x=250, y=390)

        # Use bind method
        self.ENP.bind("<Button-1>", click8)
        self.ENP.bind("<Leave>", leave)
        self.ENP['state'] = DISABLED
        # ___________| EGP = Employee Gross Pay |___________
        self.EGP = Entry(self.Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                         textvariable=self.Employee_Gross_Pay)
        # Add text in Entry box
        self.EGP.insert(0, 'Employee Gross Pay')
        self.EGP.place(x=250, y=330)

        # Use bind method
        self.EGP.bind("<Button-1>", click9)
        self.EGP.bind("<Leave>", leave)
        self.EGP['state'] = DISABLED
        # _________| Entry Box End |_________
        # _________| Button |__________

        self.cal_btn = Button(self.Manage_Frame, text="CALCULATE", width=15, font=("times new roman", 10, "bold"),
                              relief=GROOVE, bd=4, bg='teal', fg='oldlace', command=self.Calculate)
        self.cal_btn.place(x=50, y=450)
        self.cal_btn['state'] = DISABLED

        self.save_btn = Button(self.Manage_Frame, text="SAVE", width=15, font=("times new roman", 10, "bold"),
                               relief=GROOVE, bd=4, bg='teal', fg='oldlace', command=self.Save)
        self.save_btn.place(x=180, y=450)
        self.save_btn['state'] = DISABLED

        self.update_btn = Button(self.Manage_Frame, text="Update", width=15, font=("times new roman", 10, "bold"),
                                 relief=GROOVE, bd=4, bg='khaki', fg='saddlebrown', command=self.update)
        self.update_btn.place(x=310, y=450)
        self.update_btn['state'] = DISABLED

        self.del_btn = Button(self.Manage_Frame, text="Delete", width=15, font=("times new roman", 10, "bold"),
                              relief=GROOVE, bd=4, bg='red', fg='white', command=self.delete)
        self.del_btn.place(x=50, y=500)
        self.del_btn['state'] = DISABLED

        self.clear_btn = Button(self.Manage_Frame, text="CLEAR", width=15, font=("times new roman", 10, "bold"),
                                relief=GROOVE, bd=4, bg='slategray', fg='white', command=self.clear)
        self.clear_btn.place(x=180, y=500)

        self.close_btn = Button(self.Manage_Frame, text="BACK", width=15, font=("times new roman", 10, "bold"),
                                relief=GROOVE, bd=4, bg='slategray', fg='white', command=self.back)
        self.close_btn.place(x=310, y=500)
        # self.close_btn['state'] = DISABLED

        # _____| Detail Frame |________
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#2e5cbe")
        self.Detail_Frame.place(x=545, y=100, width=800, height=620)

        # -------| Search Label |---------
        lbl_search = Label(self.Detail_Frame, text="Search By", bg="#2e5cbe", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # ---------| Search ID Event and entry box Start |------------
        def NE_Search_ID(*args):
            self.NE_Search_Id.delete(0, END)

        def NE_Search_Id(*args):
            if self.NE_Search_Id.get() == 'Enter ID' or self.NE_Search_Id.get() == "":
                print('No data')
                self.fetch1()
            else:
                connect = pyodbc.connect(
                    "Driver={SQL Server};"
                    "Server=DESKTOP-SK0J9LF;"
                    "Database=Payroll_Management;"
                    "Trusted_Connection=yes;"
                )
                connect.autocommit = True

                cursor = connect.cursor()

                cursor.execute(
                    "select Employee_ID, Employee_Name, Image_Path from HBES_EI where Employee_ID Like '%" +
                    str(self.searchId.get()) + "%' and Joining_Date <= ? ", (self.Date.get(),))
                rows = cursor.fetchall()

                if not rows:
                    messagebox.showerror("Error", "No data to display")
                    print("No data in database!")
                    self.Employee_table2.focus()
                    # self.go()
                elif len(rows) != 0:
                    self.Employee_table1.delete(*self.Employee_table1.get_children())
                    for row in rows:
                        self.Employee_table1.insert('', END, text="", value=(
                            row[0], row[1], row[2]))
                    connect.autocommit = True
                connect.close()
                # self.go()

        def leave1(*args):
            self.NE_Search_Id.delete(0, END)
            self.NE_Search_Id.insert(0, 'Enter ID')
            self.Detail_Frame.focus()

        self.searchId = IntVar()
        self.NE_Search_Id = Entry(self.Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                  relief=GROOVE, textvariable=self.searchId)
        self.NE_Search_Id.grid(row=0, column=1, padx=2, pady=10)
        self.NE_Search_Id.delete(0, END)
        self.NE_Search_Id.insert(0, 'Enter ID')
        self.NE_Search_Id.bind("<Button-1>", NE_Search_ID)
        self.NE_Search_Id.bind("<KeyRelease>", NE_Search_Id)
        self.NE_Search_Id.bind("<Leave>", leave1)

        # --------| Search Name Event and entry box Start |-----------
        def NE_Search_name1(*args):
            self.NE_Search_Name.delete(0, END)

        def NE_Search_name2(*args):
            if self.NE_Search_Name.get() == 'Enter Name' or self.NE_Search_Name.get() == "":
                print('No data')
                self.fetch1()

            else:
                connect = pyodbc.connect(
                    "Driver={SQL Server};"
                    "Server=DESKTOP-SK0J9LF;"
                    "Database=Payroll_Management;"
                    "Trusted_Connection=yes;"
                )
                connect.autocommit = True

                cursor = connect.cursor()

                cursor.execute(
                    "select Employee_ID, Employee_Name, Image_Path from HBES_EI where Employee_Name Like '%" +
                    str(self.name.get()) + "%' and Joining_Date <= ? ", (self.Date.get(),))
                rows = cursor.fetchall()

                if not rows:
                    messagebox.showerror("Error", "No data to display")
                    print("No data in database!")
                    self.Employee_table2.focus()
                    # self.go()
                elif len(rows) != 0:
                    self.Employee_table1.delete(*self.Employee_table1.get_children())
                    for row in rows:
                        self.Employee_table1.insert('', END, text="", value=(row[0], row[1], row[2]))
                    connect.autocommit = True
                connect.close()
                # self.go()

        def leave2(*args):
            self.NE_Search_Name.delete(0, END)
            self.NE_Search_Name.insert(0, 'Enter Name')
            self.Detail_Frame.focus()

        self.name = StringVar()
        self.NE_Search_Name = Entry(self.Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                    relief=GROOVE, textvariable=self.name)
        self.NE_Search_Name.grid(row=0, column=2, padx=20, pady=10, sticky=W)
        self.NE_Search_Name.insert(0, 'Enter Name')
        self.NE_Search_Name.bind("<Button-1>", NE_Search_name1)
        self.NE_Search_Name.bind("<KeyRelease>", NE_Search_name2)
        self.NE_Search_Name.bind("<Leave>", leave2)

        self.print_btn = Button(self.Detail_Frame, text="Create Excel", width=15, height=2,
                                font=("times new roman", 10, "bold"),
                                relief=GROOVE, bd=4, bg='lime', fg='navy', command=self.Create_Excel)
        self.print_btn.place(x=650, y=2)

        # -------| Table Frame1 |-------

        self.Table_Frame1 = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="white")
        self.Table_Frame1.place(x=10, y=50, width=780, height=200)

        # scrollbar =  Scrollbar(Table_Frame,orient=VERTICAL)
        # scrollbar.grid(row=1,cloumn=2,sticky=N+S)
        # Table_Frame.configure(yscrollcommand=scrollbar.set)

        self.scroll_x = Scrollbar(self.Table_Frame1, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame1, orient=VERTICAL)
        self.Employee_table1 = ttk.Treeview(self.Table_Frame1, columns=(
            "Employee_ID", "Employee_Name", "Employee_Image"), xscrollcommand=self.scroll_x.set,
                                            yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.configure(command=self.Employee_table1.xview)
        self.scroll_y.configure(command=self.Employee_table1.yview)
        self.Employee_table1.heading("Employee_ID", text="Employee ID")
        self.Employee_table1.heading("Employee_Name", text="Employee Name")
        self.Employee_table1.heading("Employee_Image", text="Employee Image")
        self.Employee_table1['show'] = 'headings'
        self.Employee_table1.column("Employee_ID", width=100)
        self.Employee_table1.pack(fill=BOTH, expand=1)
        # Bind Key
        self.Employee_table1.bind("<ButtonRelease-1>", self.getcursor)
        # fetch data

        # -------| Search Label2 |--------
        lbl_search1 = Label(self.Detail_Frame, text="Search By", bg="#2e5cbe", fg="white",
                            font=("times new roman", 22, "bold"))
        lbl_search1.place(x=20, y=255)

        # ---------| Search ID Event and entry box Start |------------
        def NE_Search_ID2(*args):
            self.NE_Search_Id2.delete(0, END)

        def NE_Search_Id2(*args):
            if self.NE_Search_Id2.get() == 'Enter ID' or self.NE_Search_Id2.get() == "":
                print('No data')
                self.fetchdata()
            else:
                connect = pyodbc.connect(
                    "Driver={SQL Server};"
                    "Server=DESKTOP-SK0J9LF;"
                    "Database=Payroll_Management;"
                    "Trusted_Connection=yes;"
                )
                connect.autocommit = True

                cursor = connect.cursor()

                cursor.execute(
                    "Select e.Employee_ID, e.Employee_Name,e.Image_Path, s.Date, s.Rate, s.[Hour],s.OverTime, s.GrossPay, s.Tax, s.NetPay from Hour_Base_Employee_Salary s join HBES_EI e on s.Employee_ID = e.Employee_ID and s.Employee_ID Like '%" +
                    str(self.searchId2.get()) + "%' and Date = ?", (self.Date.get()))
                rows = cursor.fetchall()

                if not rows:
                    messagebox.showerror("Error", "No data to display")
                    print("No data in database!")
                    self.Employee_table2.focus()
                    self.fetchdata()
                    # self.go()
                elif len(rows) != 0:
                    self.Employee_table2.delete(*self.Employee_table2.get_children())
                    for row in rows:
                        self.Employee_table2.insert('', END, text="", value=(
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                    connect.autocommit = True
                connect.close()
                # self.go()

        def leave12(*args):
            self.NE_Search_Id2.delete(0, END)
            self.NE_Search_Id2.insert(0, 'Enter ID')
            self.Detail_Frame.focus()

        self.searchId2 = IntVar()
        self.NE_Search_Id2 = Entry(self.Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                   relief=GROOVE, textvariable=self.searchId2)
        self.NE_Search_Id2.place(x=170, y=260)
        self.NE_Search_Id2.delete(0, END)
        self.NE_Search_Id2.insert(0, 'Enter ID')
        self.NE_Search_Id2.bind("<Button-1>", NE_Search_ID2)
        self.NE_Search_Id2.bind("<KeyRelease>", NE_Search_Id2)
        self.NE_Search_Id2.bind("<Leave>", leave12)

        # --------| Search Name Event and entry box Start |-----------
        def NE_Search_name2(*args):
            self.NE_Search_Name2.delete(0, END)

        def NE_Search_name22(*args):
            if self.NE_Search_Name2.get() == 'Enter Name' or self.NE_Search_Name2.get() == "":
                print('No data')
                self.fetchdata()

            else:
                connect = pyodbc.connect(
                    "Driver={SQL Server};"
                    "Server=DESKTOP-SK0J9LF;"
                    "Database=Payroll_Management;"
                    "Trusted_Connection=yes;"
                )
                connect.autocommit = True

                cursor = connect.cursor()

                cursor.execute(
                    "Select e.Employee_ID, e.Employee_Name,e.Image_Path, s.Date, s.Rate, s.[Hour],s.Over_Time, s.GrossPay, s.Tax, s.NetPay from Hour_Base_Employee_Salary s join HBES_EI e on s.Employee_ID = e.Employee_ID and e.Employee_Name Like '%" +
                    str(self.name2.get()) + "%' and Date = ? ", (self.Date.get(),))
                rows = cursor.fetchall()

                if not rows:
                    messagebox.showerror("Error", "No data to display")
                    print("No data in database!")
                    self.Employee_table2.focus()
                    # self.go()
                elif len(rows) != 0:
                    self.Employee_table2.delete(*self.Employee_table2.get_children())
                    for row in rows:
                        self.Employee_table2.insert('', END, text="", value=(row[0], row[1], row[2]))
                    connect.autocommit = True
                connect.close()
                # self.go()

        def leave22(*args):
            self.NE_Search_Name2.delete(0, END)
            self.NE_Search_Name2.insert(0, 'Enter Name')
            self.Detail_Frame.focus()

        self.name2 = StringVar()
        self.NE_Search_Name2 = Entry(self.Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                     relief=GROOVE, textvariable=self.name2)
        self.NE_Search_Name2.place(x=340, y=260)
        self.NE_Search_Name2.insert(0, 'Enter Name')
        self.NE_Search_Name2.bind("<Button-1>", NE_Search_name2)
        self.NE_Search_Name2.bind("<KeyRelease>", NE_Search_name22)
        self.NE_Search_Name2.bind("<Leave>", leave22)

        # -------| Table Frame2 |-------
        self.Table_Frame2 = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="white")
        self.Table_Frame2.place(x=9, y=300, width=780, height=300)

        # scrollbar = Scrollbar(Table_Frame,orient=VERTICAL)
        # scrollbar.grid(row=1,cloumn=2,sticky=N+S)
        # Table_Frame.configure(yscrollcommand=scrollbar.set)

        self.scroll_x = Scrollbar(self.Table_Frame2, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame2, orient=VERTICAL)
        self.Employee_table2 = ttk.Treeview(self.Table_Frame2, columns=(
            "Employee_ID", "Employee_Name", "Employee_Image", "date", "Rate", "Hour", "OverTime", "Gross_Pay",
            "Employee_Tax",
            "Net_Pay"), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.configure(command=self.Employee_table2.xview)
        self.scroll_y.configure(command=self.Employee_table2.yview)
        self.Employee_table2.heading("Employee_ID", text="Employee ID")
        self.Employee_table2.heading("Employee_Name", text="Employee Name")
        self.Employee_table2.heading("Employee_Image", text="Employee Image")
        self.Employee_table2.heading("date", text="Date")
        self.Employee_table2.heading("Rate", text="Rate")
        self.Employee_table2.heading("Hour", text="Hour")
        self.Employee_table2.heading("OverTime", text="Over Time")
        self.Employee_table2.heading("Gross_Pay", text="Gross Pay")
        self.Employee_table2.heading("Employee_Tax", text="Employee Tax")
        self.Employee_table2.heading("Net_Pay", text="Net Pay")
        self.Employee_table2['show'] = 'headings'
        self.Employee_table2.column("Employee_ID", width=100)
        self.Employee_table2.pack(fill=BOTH, expand=1)
        # ------| Binding |------
        self.Employee_table2.bind("<ButtonRelease-1>", self.getcursor1)

    # ------} Clear Entry box {-----
    def clear(self):
        self.EID.delete(0, END)
        self.EID.insert(0, 'Employee ID')

        self.EN.delete(0, END)
        self.EN.insert(0, 'Employee Name')

        self.ER.delete(0, END)
        self.ER.insert(0, 'Employee Rate')

        self.EH.delete(0, END)
        self.EH.insert(0, 'Employee Hour')

        self.Employee_Image.delete(0, END)
        self.Employee_Image.insert(0, 'Employee Image')

        self.EOT.delete(0, END)
        self.EOT.insert(0, 'Employee Over Time')

        self.EGP.delete(0, END)
        self.EGP.insert(0, 'Employee Gross Pay')

        self.EIT.delete(0, END)
        self.EIT.insert(0, 'Employee Tax')

        self.ENP.delete(0, END)
        self.ENP.insert(0, 'Employee Net Pay')

    # ----} Go button {-----
    def go(self):
        self.fetch1()
        self.Employee_table2.delete(*self.Employee_table2.get_children())
        self.fetchdata()

    def fetch1(self):
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True

        cursor = connect.cursor()

        cursor.execute(
            '''
            Select Employee_ID, Employee_Name, Image_Path from HBES_EI
            where Joining_Date <= ?
            order by Employee_ID;
            ''', (self.Date.get(),))
        rows = cursor.fetchall()
        if not rows:
            print("No data in database!")
        elif len(rows) != 0:

            self.Employee_table1.delete(*self.Employee_table1.get_children())
            for row in rows:
                self.Employee_table1.insert('', END, text="", value=(row[0], row[1], row[2]))
            connect.autocommit = True
        connect.close()

    # ------} Get Cursor {-------
    def getcursor(self, ev):
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True

        cursor = connect.cursor()

        content = self.Employee_table1.item(self.Employee_table1.focus())

        row = content['values']
        print(row)
        if not row:
            print("Select Row")
        else:
            try:
                self.Employee_id.set(row[0])
                self.Employee_name.set(row[1])
                # ___| Image Code |___
                self.Employee_img.set(row[2])
                # ----| Image Label |-----
                self.lblimg = self.Employee_img.get()
                self.Uploaded = ImageTk.PhotoImage(Image.open(self.lblimg))
                upload_image_frame = Label(self.upload_image,image=self.Uploaded)
                upload_image_frame.place(x=280, y=162)
                cursor.execute(
                    '''
                    Select Date, Rate, Hour, OverTime, GrossPay, Tax, NetPay from Hour_Base_Employee_Salary where Employee_ID = ? and Date = ?

                    ''', (self.Employee_id.get(), self.Date.get())
                )
                data = cursor.fetchall()

                print(f'data {data}')
                print(type(data))

                if not data:
                    # -----| Disabled all |------
                    self.clear()
                    self.fetchdata()
                    self.Employee_id.set(row[0])
                    self.Employee_name.set(row[1])
                    # ___| Image Code |___
                    self.Employee_img.set(row[2])
                    # ----| Image Label |-----
                    self.lblimg = self.Employee_img.get()
                    self.Uploaded = ImageTk.PhotoImage(Image.open(self.lblimg))
                    upload_image_frame = Label(self.upload_image,image=self.Uploaded)
                    upload_image_frame.place(x=280, y=162)
                    self.EID['state'] = NORMAL
                    self.EN['state'] = NORMAL
                    self.ER['state'] = NORMAL
                    self.EH['state'] = NORMAL
                    self.EOT['state'] = NORMAL
                    self.EIT['state'] = NORMAL
                    self.Employee_Image['state'] = NORMAL
                    self.EGP['state'] = NORMAL
                    self.ENP['state'] = NORMAL

                    self.cal_btn['state'] = NORMAL
                    self.close_btn['state'] = NORMAL
                else:
                    messagebox.showinfo("Information", "This Employee Record Exists"
                                                       " on this date")
                    self.fetchdata()
                    self.EID['state'] = DISABLED
                    self.EN['state'] = DISABLED
                    self.ER['state'] = DISABLED
                    self.EH['state'] = DISABLED
                    self.EOT['state'] = DISABLED
                    self.EIT['state'] = DISABLED
                    self.Employee_Image['state'] = DISABLED
                    self.EGP['state'] = DISABLED
                    self.ENP['state'] = DISABLED

                    self.cal_btn['state'] = NORMAL
                    self.close_btn['state'] = NORMAL

            except Exception as e:
                print(f'Error{e}')
                messagebox.showerror("Error", "{e}")

    # -----| Fetch data fro 2 Treeview |------
    def getcursor1(self, ev):
        content = self.Employee_table2.item(self.Employee_table2.focus())
        row = content['values']
        print(row)
        if not row:
            print("Select Row")
        else:
            try:
                self.Employee_id.set(row[0])
                self.Employee_name.set(row[1])
                # ___| Image Code |___
                self.Employee_img.set(row[2])
                # ----| Image Label |-----
                self.lblimg = self.Employee_img.get()
                self.Uploaded = ImageTk.PhotoImage(Image.open(self.lblimg))
                upload_image_frame = Label(self.upload_image,image=self.Uploaded)
                upload_image_frame.place(x=280, y=162)

                self.Date.set(row[3])
                self.Employee_Rate.set(row[4])
                self.Employee_Hour.set(row[5])
                self.EOT.delete(0, END)
                self.EOT.insert(0, row[6])
                self.EGP.delete(0, END)
                self.EGP.insert(0, row[7])
                self.Employee_Income_Tax.set(row[8])
                self.ENP.delete(0, END)
                self.ENP.insert(0, row[9])
                self.save_btn['state'] = DISABLED
                self.EID['state'] = NORMAL
                self.EN['state'] = NORMAL
                self.ER['state'] = NORMAL
                self.EH['state'] = NORMAL
                self.EOT['state'] = NORMAL
                self.EIT['state'] = NORMAL
                self.Employee_Image['state'] = NORMAL
                self.EGP['state'] = NORMAL
                self.ENP['state'] = NORMAL

                self.cal_btn['state'] = NORMAL
                self.update_btn['state'] = NORMAL
                self.del_btn['state'] = NORMAL
                self.close_btn['state'] = NORMAL
            except:
                print(f'Error')

    # -----| calculation |------
    def Calculate(self):
        if self.ER.get() == 'Employee Rate':
            messagebox.showerror("Error", "Please Insert Employee Rate")

        elif self.EH.get() == 'Employee Hour':
            messagebox.showerror("Error", "Please Insert Employee Hour")

        # elif self.EOT.get() != 'Employee Over Time':
        #     self.Overtime = self.Employee_Overtime.get()

        elif self.EOT.get() == 'Employee Over Time':
            e = messagebox.askquestion("Confirmation", "Do You Want to add Employee OverTIme")
            if e == 'yes':
                self.EOT.delete(0, END)
                self.EOT.focus()
                self.Overtime = self.Employee_Overtime
            else:
                self.EOT.delete(0, END)
                self.EOT.insert(0, 0)

        elif self.EIT.get() == 'Employee Tax':
            messagebox.showerror("Error", "Please Enter Employee Tax")

        else:
            # ----| Store Value in Variables |----
            self.Overtime = float(self.EOT.get())
            print(self.Overtime)
            self.Hour = self.Employee_Hour.get()
            self.Rate = self.Employee_Rate.get()
            self.Tax = self.EIT.get()
            print(f"Employee Hour {self.Hour}")
            print(f"Employee Rate {self.Rate}")
            print(f"Employee Overtime {self.Overtime}")
            # ----| Claculatioon for Gross pay |----
            self.GrossPay1 = self.Rate * self.Hour
            print(self.GrossPay1)
            self.GrossPay2 = self.Overtime * self.Rate
            self.GrossPay = self.GrossPay1 + self.GrossPay2
            print(self.GrossPay)
            # print(f"Gross Pay {self.GrossPay}")
            print(type(self.GrossPay))
            self.EGP.delete(0, END)
            self.EGP.insert(0, self.GrossPay)

            # ----| Calculation for Net pay |----
            self.NetPay = float(self.GrossPay) - int(self.Tax)
            # print(f"Net Pay {self.NetPay}")
            self.ENP.delete(0, END)
            self.ENP.insert(0, self.NetPay)

            self.save_btn['state'] = NORMAL

    # ------| Save Function |-------
    def Save(self):
        print("Saving...")
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True
        cursor = connect.cursor()
        self.records = [self.Employee_id.get(), self.Date.get(), self.Employee_Rate.get(), self.Employee_Hour.get(),
                        self.EOT.get(), self.EGP.get(), self.EIT.get(), self.ENP.get()]
        self.insert_query = "Insert into Hour_Base_Employee_Salary(Employee_ID, Date, Rate, Hour, OverTime, GrossPay, Tax, NetPay) Values (?, ?, ?, ?, ?, ?, ?, ?);"
        cursor.execute(self.insert_query, self.records)
        # self.go()
        connect.commit()
        connect.close()
        self.fetchdata()
        messagebox.showinfo("Information", "Record Updated Successfully( ' * ' )")
        self.clear()
        self.save_btn['state'] = DISABLED


    def fetchdata(self):
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True

        cursor = connect.cursor()

        cursor.execute(
            '''
            Select e.Employee_ID, e.Employee_Name,e.Image_Path, s.Date, s.Rate, s.[Hour], s.OverTime, s.GrossPay, s.Tax, s.NetPay from Hour_Base_Employee_Salary s join HBES_EI e on s.Employee_ID = e.Employee_ID
            and Date = ?
            order by Employee_ID;
            ''', (self.Date.get()))
        rows = cursor.fetchall()
        if not rows:
            print("No data in database!")
        elif len(rows) != 0:
            self.Employee_table2.delete(*self.Employee_table2.get_children())
            for row in rows:
                self.Employee_table2.insert('', END, text="", value=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            connect.autocommit = True
        connect.close()

    def update(self):
        print('Update')
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True

        cursor = connect.cursor()

        cursor.execute(
            "Update Payroll_Management.dbo.Hour_Base_Employee_Salary set Date = ?, Rate = ?, Hour = ?, OverTime = ?, GrossPay = ?, Tax = ?, NetPay = ? where Employee_ID = ?",
            (
                self.Date.get(),
                self.Employee_Rate.get(),
                self.Employee_Hour.get(),
                self.EOT.get(),
                self.EGP.get(),
                self.EIT.get(),
                self.ENP.get(),
                self.Employee_id.get()
            )
        )
        # self.go()
        connect.commit()
        connect.close()
        self.Employee_table2.delete(*self.Employee_table2.get_children())
        self.fetchdata()
        messagebox.showinfo("Information", "Record Updated Successfully( ' * ' )")
        self.clear()

    def delete(self):
        print('delete')
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True

        cursor = connect.cursor()

        cursor.execute(
            "Delete from Payroll_Management.dbo.Hour_Base_Employee_Salary where Employee_ID = ?",
            (
                self.Employee_id.get()
            )
        )
        # self.go()
        connect.commit()
        connect.close()
        self.Employee_table2.delete(*self.Employee_table2.get_children())
        self.fetchdata()
        messagebox.showinfo("Information", "Record Updated Successfully( ' * ' )")
        self.clear()

    def clear(self):
        self.EID.delete(0, END)
        self.EID.insert(0, 'Employee ID')

        self.EN.delete(0, END)
        self.EN.insert(0, 'Employee Name')

        self.ER.delete(0, END)
        self.ER.insert(0, 'Employee Rate')

        self.EH.delete(0, END)
        self.EH.insert(0, 'Employee Hour')

        self.Employee_Image.delete(0, END)
        self.Employee_Image.insert(0, 'Employee Image')

        self.EOT.delete(0, END)
        self.EOT.insert(0, 'Employee Over Time')

        self.EGP.delete(0, END)
        self.EGP.insert(0, 'Employee Gross Pay')

        self.EIT.delete(0, END)
        self.EIT.insert(0, 'Employee Tax')

        self.ENP.delete(0, END)
        self.ENP.insert(0, 'Employee Net Pay')

    def Create_Excel(self):
        print("Creating Excel...")
        # ---| Excel Sheet Creating start |---
        import pandas as pd
        data = [self.Employee_table2.item(item)['values'] for item in self.Employee_table2.get_children()]
        df = pd.DataFrame(data)
        df.to_csv('HourlyBaseEmployeeSalary.csv', encoding='shift-jis', header=['Employee ID','Employee Name','Employee Image','Date','Rate','Hour','OverTime','Gross Pay','Employee Tax','Net Pay'], index=False)

    def back(self):
        self.root.destroy()
        # dashboard_Window = Tk()
        # obj = Dashboard_Window(dashboard_Window)
        # dashboard_Window.mainloop()






# root = Tk()
# obj = HBES(root)
# root.mainloop()
