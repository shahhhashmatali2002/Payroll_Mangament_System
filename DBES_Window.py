from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkcalendar import Calendar
import pyodbc

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

table = "Daily_Base_Employee_Salary"

# Asking user to enter database name he wants to check
# database_name = input('Enter database name to check exist or not: ')
cur = conn.cursor()
cur.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?;", (table,))
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
        '''Create table Daily_Base_Employee_Salary(
            Salary_ID int Identity(1,1),
            Employee_ID int,
            Date date,
            Amount int,
            Employee_Over_Time float,
            Gross_Pay float,
            Tax int,
            Net_Pay float,
            Constraint PK_Daily_Base_Employee_Salary Primary Key (Salary_ID),
            FOREIGN KEY (Employee_ID) REFERENCES DBES_EI(Employee_ID)

                                )'''
    )
    print(" '{}' table Successfully Create in Payroll_Management Database".format(table))
else:
    print(" '{}' table Exist in Payroll_Management Database".format(table))


class CDBES:
    def __init__(self, root):
        self.DBES_root = root
        self.DBES_root.title('Daily Base Amount')
        self.DBES_root.geometry('1360x768+0+0')
        self.DBES_root.resizable(0, 0)
        self.title = Label(self.DBES_root, text="DAILY BASE EMPLOYEE SALARY", bd=4, font=("times new roman", 40),
                           bg="gray",
                           fg="black", relief=GROOVE, justify=CENTER)
        self.title.pack(side=TOP, fill=X)
        # ________| Manage Frame |___________
        self.DBES_Manage_Frame = Frame(self.DBES_root, bd=4, relief=RIDGE, bg="gray")
        self.DBES_Manage_Frame.place(x=20, y=100, width=500, height=620)

        # ______| Function for Entry placeholder removing |__________
        def click1(*args):
            if self.DBES_EID['state'] != DISABLED:
                messagebox.showinfo("Information",
                                    "Please Don't try to insert\nBecause Employee ID Fetch from Treeview")
                return "break"

        def click2(*args):
            if self.DBES_EN['state'] != DISABLED:
                messagebox.showinfo("Information",
                                    "Please Don't try to insert\nBecause Employee Name Fetch from Treeview")
                return "break"

        def click3(event):
            if self.DBES_ES.get() == 'Amount':
                self.DBES_ES.delete(0, END)

        def click4(*args):
            self.DBES_EOT.focus()
            self.DBES_EOT.delete(0, END)

        def click6(*args):
            self.DBES_EIT.focus()
            if self.DBES_EIT.get() == 'Employee Tax':
                self.DBES_EIT.focus()
                self.DBES_EIT.delete(0, 'end')

        def click8(*args):
            messagebox.showinfo("Information", "Click on Calculate Button Value Auto Set")
            return "break"

        def click9(*args):
            messagebox.showinfo("Information", "Click on Calculate Button Value Auto Set")
            return "break"

            # ________| leave Function |_________

        def leave(*args):
            self.DBES_Manage_Frame.focus()
            if self.Employee_id.get() == "":
                self.DBES_EID.insert(0, 'Employee ID')
                self.DBES_Manage_Frame.focus()
            elif self.Employee_name.get() == "":
                self.DBES_EN.insert(0, 'Employee Name')
                self.DBES_Manage_Frame.focus()
            elif self.DBES_ES.get() == "":
                self.DBES_ES.insert(0, 'Amount')
                self.DBES_Manage_Frame.focus()
            elif self.DBES_EOT.get() == "":
                self.DBES_EOT.insert(0, 0)
                self.DBES_Manage_Frame.focus()

            # _-_-) Data Enter in Employee Gross Pay (_-_
            elif self.DBES_EGP.get() == "":
                self.DBES_EGP.insert(0, 'Employee Gross Pay')
                self.DBES_Manage_Frame.focus()
            elif self.DBES_EIT.get() == "":
                self.DBES_EIT.insert(0, 'Employee Tax')
                self.DBES_Manage_Frame.focus()
            elif self.DBES_ENP.get() == "":
                self.DBES_ENP.insert(0, 'Employee Net Pay')
                self.DBES_Manage_Frame.focus()

        # call function when we  entry box
        self.Date = StringVar()
        self.Employee_id = StringVar()
        self.Employee_name = StringVar()
        self.Employee_Salary = IntVar()
        self.Employee_Overtime = float()
        self.Employee_Gross_Pay = float
        self.Employee_Income_Tax = IntVar()
        self.Employee_Company_Tax = StringVar()
        self.Employee_Net_Pay = float
        self.Employee_img = StringVar()

        # #________| Date Pciker |________
        Label(self.DBES_Manage_Frame, text="Date: ", bg="gray", fg="black", font=("times new roman", 20, "bold")).place(
            x=10, y=10)
        cal = DateEntry(self.DBES_Manage_Frame, textvariable=self.Date, width=10, day=1, month=1, year=2021,
                        background='darkblue', foreground='white', borderwidth=2, font=("times new roman", 15, "bold"),
                        state='readonly')
        cal.place(x=100, y=20)

        self.DEBS_go_btn = Button(self.DBES_Manage_Frame, text='GO', width=10, font=("times new roman", 10, "bold"),
                                  relief=GROOVE,
                                  bd=4, bg='teal', fg='black', command=self.go)
        self.DEBS_go_btn.place(x=250, y=18)
        # Manage_Frame.focus()

        # ______| Upload Image Frame |_______

        self.upload_image = Frame(self.DBES_Manage_Frame, width=192, height=192).place(x=260, y=60)

        def NE_EI(*args):
            messagebox.showinfo("Information",
                                "Please dont't try to Insert Image Path\nBecause Image Path Fetch from Database!")
            return "break"

        self.DBES_Employee_Image = Entry(self.DBES_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                                         textvariable=self.Employee_img)
        self.DBES_Employee_Image.place(x=250, y=270)
        self.DBES_Employee_Image.insert(0, 'Employee Image')
        self.DBES_Employee_Image.bind("<Button-1>", NE_EI)
        self.DBES_Employee_Image['state'] = DISABLED

        # ________| Entry Box Start |_______
        # _________| EID = Employee ID (Entry Box) |_________
        self.DBES_EID = Entry(self.DBES_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                              textvariable=self.Employee_id)

        # Add text in Entry box
        self.DBES_EID.insert(0, 'Employee ID')
        self.DBES_EID.place(x=20, y=90)

        # Use bind method
        self.DBES_EID.bind("<Button-1>", click1)
        self.DBES_EID.bind("<Leave>", leave)
        self.DBES_EID['state'] = DISABLED

        # ________| EN = Employee Name (Entry Box) |________
        self.DBES_EN = Entry(self.DBES_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                             textvariable=self.Employee_name)

        # Add text in Entry box
        self.DBES_EN.insert(0, 'Employee Name')
        self.DBES_EN.place(x=20, y=150)

        # Use bind method
        self.DBES_EN.bind("<Button-1>", click2)
        self.DBES_EN.bind("<Leave>", leave)
        self.DBES_EN['state'] = DISABLED

        # __________| ER = Amount (Entry Box) |_____________

        # _-_-_-_-_| Function not allo |_-_-_-_-_-_
        def only_allow(event):
            char = event.char.lower()
            if (event.state & 3) >> 2:
                return None

            if char.isprintable() and (not event.char.isdigit()):
                messagebox.showerror("Error", "String Not Allow\nPlease Enter Number")
                return "break"
            elif len(self.DBES_ES.get()) > 6:
                self.DBES_ES.focus()
                # NE_nic.focus()
                return "break"

        self.DBES_ES = Entry(self.DBES_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                             textvariable=self.Employee_Salary)
        # Add text in Entry box
        self.DBES_ES.delete(0, END)
        self.DBES_ES.insert(0, 'Amount')
        self.DBES_ES.place(x=20, y=210)

        # Use bind method
        self.DBES_ES.bind("<Button-1>", click3)
        self.DBES_ES.bind("<Leave>", leave)
        self.DBES_ES.bind("<Key>", only_allow)
        self.DBES_ES['state'] = DISABLED

        # __________| EH = Employee Absent (Entry Box) |____________

        # __________| EOT = Employee Over Time (Entry Box) |____________

        def not_allow_EOT(event):
            char = event.char.lower()

            if (event.state & 3) >> 2:
                return None

            if char.isprintable() and (not event.char.isdigit()):
                messagebox.showerror("Error", "String Not Allow\nPlease Enter Number")
                return "break"
            elif len(self.DBES_EOT.get()) > 0:
                self.DBES_EOT.focus()
                return "break"

        self.DBES_EOT = Entry(self.DBES_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                              textvariable=self.Employee_Overtime)
        # Add text in Entry box
        self.DBES_EOT.delete(0, END)
        self.DBES_EOT.insert(0, 'Employee Over Time')
        self.DBES_EOT.place(x=20, y=270)

        # Use bind method
        self.DBES_EOT.bind("<Button-1>", click4)
        self.DBES_EOT.bind("<Leave>", leave)
        self.DBES_EOT.bind("<Key>", not_allow_EOT)
        self.DBES_EOT['state'] = DISABLED
        # ___________| EIT = Employee Income Tax |___________
        self.DBES_EIT = Entry(self.DBES_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                              textvariable=self.Employee_Income_Tax)
        # Add text in Entry box
        self.DBES_EIT.delete(0, END)
        self.DBES_EIT.insert(0, 'Employee Tax')
        self.DBES_EIT.place(x=250, y=330)

        # Use bind method
        self.DBES_EIT.bind("<Button-1>", click6)
        self.DBES_EIT.bind("<Leave>", leave)
        self.DBES_EIT['state'] = DISABLED

        # ___________| ENP = Employee Net Pay |___________
        self.DBES_ENP = Entry(self.DBES_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                              textvariable=self.Employee_Net_Pay)
        # Add text in Entry box
        self.DBES_ENP.insert(0, 'Employee Net Pay')
        self.DBES_ENP.place(x=20, y=390)

        # Use bind method
        self.DBES_ENP.bind("<Button-1>", click8)
        self.DBES_ENP.bind("<Leave>", leave)
        self.DBES_ENP['state'] = DISABLED
        # ___________| EGP = Employee Gross Pay |___________
        self.DBES_EGP = Entry(self.DBES_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                              textvariable=self.Employee_Gross_Pay)
        # Add text in Entry box
        self.DBES_EGP.insert(0, 'Employee Gross Pay')
        self.DBES_EGP.place(x=20, y=330)

        # Use bind method
        self.DBES_EGP.bind("<Button-1>", click9)
        self.DBES_EGP.bind("<Leave>", leave)
        self.DBES_EGP['state'] = DISABLED
        # _________| Entry Box End |_________
        # _________| Button |__________

        self.DBES_cal_btn = Button(self.DBES_Manage_Frame, text="CALCULATE", width=15,
                                   font=("times new roman", 10, "bold"),
                                   relief=GROOVE, bd=4, bg='teal', fg='black', command=self.Calculate)
        self.DBES_cal_btn.place(x=50, y=450)
        self.DBES_cal_btn['state'] = DISABLED

        self.DBES_save_btn = Button(self.DBES_Manage_Frame, text="SAVE", width=15, font=("times new roman", 10, "bold"),
                                    relief=GROOVE, bd=4, bg='teal', fg='black', command=self.Save)
        self.DBES_save_btn.place(x=180, y=450)
        self.DBES_save_btn['state'] = DISABLED

        self.DBES_update_btn = Button(self.DBES_Manage_Frame, text="Update", width=15,
                                      font=("times new roman", 10, "bold"),
                                      relief=GROOVE, bd=4, bg='khaki', fg='black', command=self.update)
        self.DBES_update_btn.place(x=310, y=450)
        self.DBES_update_btn['state'] = DISABLED

        self.DBES_del_btn = Button(self.DBES_Manage_Frame, text="Delete", width=15,
                                   font=("times new roman", 10, "bold"),
                                   relief=GROOVE, bd=4, bg='red', fg='black', command=self.delete)
        self.DBES_del_btn.place(x=50, y=500)
        self.DBES_del_btn['state'] = DISABLED

        self.DBES_clear_btn = Button(self.DBES_Manage_Frame, text="CLEAR", width=15,
                                     font=("times new roman", 10, "bold"),
                                     relief=GROOVE, bd=4, bg='slategray', fg='black', command=self.clear)
        self.DBES_clear_btn.place(x=180, y=500)

        self.DVES_close_btn = Button(self.DBES_Manage_Frame, text="CLOSE", width=15,
                                     font=("times new roman", 10, "bold"),
                                     relief=GROOVE, bd=4, bg='slategray', fg='black', command=lambda: exit())
        self.DVES_close_btn.place(x=310, y=500)
        # close_btn['state'] = DISABLED

        # _____| Detail Frame |________
        self.DBES_Detail_Frame = Frame(self.DBES_root, bd=4, relief=RIDGE, bg="gray")
        self.DBES_Detail_Frame.place(x=545, y=100, width=800, height=620)

        # -------| Search Label |---------
        self.DBES_lbl_search = Label(self.DBES_Detail_Frame, text="Search By", bg="gray", fg="black",
                                     font=("times new roman", 20, "bold"))
        self.DBES_lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # ---------| Search ID Event and entry box Start |------------
        def NE_Search_ID(*args):
            self.DBES_NE_Search_Id.delete(0, END)

        def NE_Search_Id(*args):
            if self.DBES_NE_Search_Id.get() == 'Enter ID' or self.DBES_NE_Search_Id.get() == "":
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
                    "select Employee_ID, Employee_Name, Employee_Image from DBES_EI where Employee_ID Like '%" +
                    str(self.DBES_NE_Search_Id.get()) + "%' and Joining_Date <= ? ", (self.Date.get(),))
                rows = cursor.fetchall()

                if not rows:
                    self.DBES_Employee_table1.delete(*self.DBES_Employee_table1.get_children())
                    messagebox.showerror("Error", "No data to display")
                    print("No data in database!")
                    self.DBES_Employee_table2.focus()
                    self.go()
                elif len(rows) != 0:
                    self.DBES_Employee_table1.delete(*self.DBES_Employee_table1.get_children())
                    for row in rows:
                        self.DBES_Employee_table1.insert('', END, text="", value=(
                            row[0], row[1], row[2]))
                    connect.autocommit = True
                connect.close()
                # go()

        def leave1(*args):
            self.DBES_NE_Search_Id.delete(0, END)
            self.DBES_NE_Search_Id.insert(0, 'Enter ID')
            self.DBES_Detail_Frame.focus()

        self.searchId = IntVar()
        self.DBES_NE_Search_Id = Entry(self.DBES_Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                       relief=GROOVE, textvariable=self.searchId)
        self.DBES_NE_Search_Id.grid(row=0, column=1, padx=2, pady=10)
        self.DBES_NE_Search_Id.delete(0, END)
        self.DBES_NE_Search_Id.insert(0, 'Enter ID')
        self.DBES_NE_Search_Id.bind("<Button-1>", NE_Search_ID)
        self.DBES_NE_Search_Id.bind("<KeyRelease>", NE_Search_Id)
        self.DBES_NE_Search_Id.bind("<Leave>", leave1)

        # --------| Search Name Event and entry box Start |-----------
        def NE_Search_name1(*args):
            self.DBES_NE_Search_Name.delete(0, END)

        def NE_Search_name2(*args):
            if self.DBES_NE_Search_Name.get() == 'Enter Name' or self.DBES_NE_Search_Name.get() == "":
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
                    "select Employee_ID, Employee_Name, Employee_Image from DBES_EI where Employee_Name Like '%" +
                    str(self.name.get()) + "%' and Joining_Date <= ? ", (self.Date.get(),))
                rows = cursor.fetchall()

                if not rows:
                    self.DBES_Employee_table1.delete(*self.DBES_Employee_table1.get_children())
                    messagebox.showerror("Error", "No data to display")
                    print("No data in database!")
                    self.DBES_Employee_table2.focus()
                    self.go()
                elif len(rows) != 0:
                    self.DBES_Employee_table1.delete(*self.DBES_Employee_table1.get_children())
                    for row in rows:
                        self.DBES_Employee_table1.insert('', END, text="", value=(row[0], row[1], row[2]))
                    connect.autocommit = True
                connect.close()

        def leave2(*args):
            self.DBES_NE_Search_Name.delete(0, END)
            self.DBES_NE_Search_Name.insert(0, 'Enter Name')
            self.DBES_Detail_Frame.focus()

        self.name = StringVar()
        self.DBES_NE_Search_Name = Entry(self.DBES_Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                         relief=GROOVE, textvariable=self.name)
        self.DBES_NE_Search_Name.grid(row=0, column=2, padx=20, pady=10, sticky=W)
        self.DBES_NE_Search_Name.insert(0, 'Enter Name')
        self.DBES_NE_Search_Name.bind("<Button-1>", NE_Search_name1)
        self.DBES_NE_Search_Name.bind("<KeyRelease>", NE_Search_name2)
        self.DBES_NE_Search_Name.bind("<Leave>", leave2)

        self.DBES_print_btn = Button(self.DBES_Detail_Frame, text="Create Excel", width=15, height=2,
                                     font=("times new roman", 10, "bold"),
                                     relief=GROOVE, bd=4, bg='lime', fg='navy', command=self.Create_Excel)
        self.DBES_print_btn.place(x=650, y=2)

        # -------| Table Frame1 |-------

        self.DBES_Table_Frame1 = Frame(self.DBES_Detail_Frame, bd=4, relief=RIDGE, bg="black")
        self.DBES_Table_Frame1.place(x=10, y=50, width=780, height=200)

        # scrollbar =  Scrollbar(Table_Frame,orient=VERTICAL)
        # scrollbar.grid(row=1,cloumn=2,sticky=N+S)
        # Table_Frame.configure(yscrollcommand=scrollbar.set)

        self.scroll_x = Scrollbar(self.DBES_Table_Frame1, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.DBES_Table_Frame1, orient=VERTICAL)
        self.DBES_Employee_table1 = ttk.Treeview(self.DBES_Table_Frame1, columns=(
            "Employee_ID", "Employee_Name", "Employee_Image"), xscrollcommand=self.scroll_x.set,
                                                 yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.configure(command=self.DBES_Employee_table1.xview)
        self.scroll_y.configure(command=self.DBES_Employee_table1.yview)
        self.DBES_Employee_table1.heading("Employee_ID", text="Employee ID")
        self.DBES_Employee_table1.heading("Employee_Name", text="Employee Name")
        self.DBES_Employee_table1.heading("Employee_Image", text="Employee Image")
        self.DBES_Employee_table1['show'] = 'headings'
        self.DBES_Employee_table1.column("Employee_ID", width=100)
        self.DBES_Employee_table1.pack(fill=BOTH, expand=1)
        # Bind Key
        self.DBES_Employee_table1.bind("<ButtonRelease-1>", self.getcursor)
        # fetch data

        # -------| Search Label2 |--------
        self.DBES_lbl_search1 = Label(self.DBES_Detail_Frame, text="Search By", bg="gray", fg="black",
                                      font=("times new roman", 22, "bold"))
        self.DBES_lbl_search1.place(x=20, y=255)

        # ---------| Search ID Event and entry box Start |------------
        def NE_Search_ID2(*args):
            self.DBES_NE_Search_Id2.delete(0, END)

        def NE_Search_Id2(*args):
            if self.DBES_NE_Search_Id2.get() == 'Enter ID' or self.DBES_NE_Search_Id2.get() == "":
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
                    "Select e.Employee_ID, e.Employee_Name,e.Employee_Image, s.Date, s.Amount, s.Employee_Over_Time, s.Gross_Pay, s.Tax, s.Net_Pay from Daily_Base_Employee_Salary s join DBES_EI e on s.Employee_ID = e.Employee_ID and s.Employee_ID Like '%" +
                    str(self.searchId2.get()) + "%' and s.Date = ?", (self.Date.get()))
                rows = cursor.fetchall()

                if not rows:
                    self.DBES_Employee_table2.delete(*self.DBES_Employee_table2.get_children())
                    messagebox.showerror("Error", "No data to display")
                    print("No data in database!")
                    self.DBES_Employee_table2.focus()
                    self.fetchdata()
                    # go()
                elif len(rows) != 0:
                    self.DBES_Employee_table2.delete(*self.DBES_Employee_table2.get_children())
                    for row in rows:
                        self.DBES_Employee_table2.insert('', END, text="", value=(
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                    connect.autocommit = True
                connect.close()
            # go()

        def leave12(*args):
            self.DBES_NE_Search_Id2.delete(0, END)
            self.DBES_NE_Search_Id2.insert(0, 'Enter ID')
            self.DBES_Detail_Frame.focus()

        self.searchId2 = IntVar()
        self.DBES_NE_Search_Id2 = Entry(self.DBES_Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                        relief=GROOVE, textvariable=self.searchId2)
        self.DBES_NE_Search_Id2.place(x=170, y=260)
        self.DBES_NE_Search_Id2.delete(0, END)
        self.DBES_NE_Search_Id2.insert(0, 'Enter ID')
        self.DBES_NE_Search_Id2.bind("<Button-1>", NE_Search_ID2)
        self.DBES_NE_Search_Id2.bind("<KeyRelease>", NE_Search_Id2)
        self.DBES_NE_Search_Id2.bind("<Leave>", leave12)

        # --------| Search Name Event and entry box Start |-----------
        def NE_Search_name2(*args):
            self.DBES_NE_Search_Name2.delete(0, END)

        def NE_Search_name22(*args):
            if self.DBES_NE_Search_Name2.get() == 'Enter Name' or self.DBES_NE_Search_Name2.get() == "":
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
                    "Select e.Employee_ID, e.Employee_Name,e.Employee_Image, s.Date, s.Amount, s.Employee_Over_Time, s.Gross_Pay, s.Tax, s.Net_Pay from Daily_Base_Employee_Salary s join DBES_EI e on s.Employee_ID = e.Employee_ID and e.Employee_Name Like '%" +
                    str(self.name2.get()) + "%' and s.Date = ? ", (self.Date.get(),))
                rows = cursor.fetchall()

                if not rows:
                    self.DBES_Employee_table2.delete(*self.DBES_Employee_table2.get_children())
                    messagebox.showerror("Error", "No data to display")
                    print("No data in database!")
                    self.DBES_Employee_table2.focus()
                    self.fetchdata()
                    # go()
                elif len(rows) != 0:
                    self.DBES_Employee_table2.delete(*self.DBES_Employee_table2.get_children())
                    for row in rows:
                        self.DBES_Employee_table2.insert('', END, text="", value=(
                            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
                    connect.autocommit = True
                connect.close()
            # go()

        def leave22(*args):
            self.DBES_NE_Search_Name2.delete(0, END)
            self.DBES_NE_Search_Name2.insert(0, 'Enter Name')
            self.DBES_Detail_Frame.focus()

        self.name2 = StringVar()
        self.DBES_NE_Search_Name2 = Entry(self.DBES_Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                          relief=GROOVE, textvariable=self.name2)
        self.DBES_NE_Search_Name2.place(x=340, y=260)
        self.DBES_NE_Search_Name2.insert(0, 'Enter Name')
        self.DBES_NE_Search_Name2.bind("<Button-1>", NE_Search_name2)
        self.DBES_NE_Search_Name2.bind("<KeyRelease>", NE_Search_name22)
        self.DBES_NE_Search_Name2.bind("<Leave>", leave22)

        # -------| Table Frame2 |-------
        self.DBES_Table_Frame2 = Frame(self.DBES_Detail_Frame, bd=4, relief=RIDGE, bg="white")
        self.DBES_Table_Frame2.place(x=9, y=300, width=780, height=300)

        # scrollbar = Scrollbar(Table_Frame,orient=VERTICAL)
        # scrollbar.grid(row=1,cloumn=2,sticky=N+S)
        # Table_Frame.configure(yscrollcommand=scrollbar.set)

        self.scroll_x = Scrollbar(self.DBES_Table_Frame2, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.DBES_Table_Frame2, orient=VERTICAL)
        self.DBES_Employee_table2 = ttk.Treeview(self.DBES_Table_Frame2, columns=(
            "Employee_ID", "Employee_Name", "Employee_Image", "date", "Amount", "OverTime", "Gross_Pay",
            "Employee_Tax",
            "Net_Pay"), xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.configure(command=self.DBES_Employee_table2.xview)
        self.scroll_y.configure(command=self.DBES_Employee_table2.yview)
        self.DBES_Employee_table2.heading("Employee_ID", text="Employee ID")
        self.DBES_Employee_table2.heading("Employee_Name", text="Employee Name")
        self.DBES_Employee_table2.heading("Employee_Image", text="Employee Image")
        self.DBES_Employee_table2.heading("date", text="Date")
        self.DBES_Employee_table2.heading("Amount", text="Amount")
        self.DBES_Employee_table2.heading("OverTime", text="Over Time")
        self.DBES_Employee_table2.heading("Gross_Pay", text="Gross Pay")
        self.DBES_Employee_table2.heading("Employee_Tax", text="Employee Tax")
        self.DBES_Employee_table2.heading("Net_Pay", text="Net Pay")
        self.DBES_Employee_table2['show'] = 'headings'
        self.DBES_Employee_table2.column("Employee_ID", width=100)
        self.DBES_Employee_table2.pack(fill=BOTH, expand=1)
        # ------| Binding |------
        self.DBES_Employee_table2.bind("<ButtonRelease-1>", self.getcursor1)

    # ------} Clear Entry box {-----
    def clear(self):
        self.DBES_EID.delete(0, END)
        self.DBES_EID.insert(0, 'Employee ID')

        self.DBES_EN.delete(0, END)
        self.DBES_EN.insert(0, 'Employee Name')

        self.DBES_ES.delete(0, END)
        self.DBES_ES.insert(0, 'Amount')

        self.DBES_Employee_Image.delete(0, END)
        self.DBES_Employee_Image.insert(0, 'Employee Image')

        self.DBES_EOT.delete(0, END)
        self.DBES_EOT.insert(0, 'Employee Over Time')

        self.DBES_EGP.delete(0, END)
        self.DBES_EGP.insert(0, 'Employee Gross Pay')

        self.DBES_EIT.delete(0, END)
        self.DBES_EIT.insert(0, 'Employee Tax')

        self.DBES_ENP.delete(0, END)
        self.DBES_ENP.insert(0, 'Employee Net Pay')

        # ----} Go button {-----

    def go(self):
        print('going...')
        self.DBES_Employee_table2.delete(*self.DBES_Employee_table2.get_children())
        self.fetch1()
        self.fetchdata()

    def fetch1(self):
        print('fetching...')
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
            Select Employee_ID, Employee_Name, Employee_Image from DBES_EI
            where Joining_Date <= ?
            order by Employee_ID;
            ''', (self.Date.get(),))
        rows = cursor.fetchall()
        if not rows:
            print("No data in database!")
            self.DBES_Employee_table1.delete(*self.DBES_Employee_table1.get_children())
            messagebox.showinfo("Information", "No data to display")
        elif len(rows) != 0:

            self.DBES_Employee_table1.delete(*self.DBES_Employee_table1.get_children())
            for row in rows:
                self.DBES_Employee_table1.insert('', END, text="", value=(row[0], row[1], row[2]))
            connect.autocommit = True
        connect.close()

    # ------} Get Cursor {-------
    def getcursor(self, ev):
        print('getting...')
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True

        cursor = connect.cursor()

        content = self.DBES_Employee_table1.item(self.DBES_Employee_table1.focus())

        row = content['values']
        # print(row)
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
                self.upload_image_frame = Label(self.upload_image, image=self.Uploaded)
                self.upload_image_frame.place(x=280, y=162)
                cursor.execute(
                    '''
                    Select Date, Amount, Employee_Over_Time, Gross_Pay, Tax, Net_Pay from Daily_Base_Employee_Salary where Employee_ID = ? and Date = ?

                    ''', (self.Employee_id.get(), self.Date.get())
                )
                fetching = cursor.fetchall()

                print(f'data {data}')
                print(type(data))

                if not fetching:
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
                    self.upload_image_frame = Label(self.upload_image, image=self.Uploaded)
                    self.upload_image_frame.place(x=280, y=162)
                    self.DBES_EID['state'] = NORMAL
                    self.DBES_EN['state'] = NORMAL
                    self.DBES_ES['state'] = NORMAL
                    self.DBES_EOT['state'] = NORMAL
                    self.DBES_EIT['state'] = NORMAL
                    self.DBES_Employee_Image['state'] = NORMAL
                    self.DBES_EGP['state'] = NORMAL
                    self.DBES_ENP['state'] = NORMAL

                    self.DBES_cal_btn['state'] = NORMAL
                    self.DVES_close_btn['state'] = NORMAL
                else:
                    messagebox.showinfo("Information", "This Employee Record Exists"
                                                       " on this date")
                    self.fetchdata()
                    self.DBES_EID['state'] = DISABLED
                    self.DBES_EN['state'] = DISABLED
                    self.DBES_ES['state'] = DISABLED
                    self.DBES_EOT['state'] = DISABLED
                    self.DBES_EIT['state'] = DISABLED
                    self.DBES_Employee_Image['state'] = DISABLED
                    self.DBES_EGP['state'] = DISABLED
                    self.DBES_ENP['state'] = DISABLED
                    self.DBES_del_btn['state'] = DISABLED
                    self.DBES_update_btn['state'] = DISABLED
                    self.DBES_cal_btn['state'] = NORMAL

            except Exception as e:
                print(f'Error{e}')
                messagebox.showerror("Error", "{e}")

    # -----| Fetch data fro 2 Treeview |------
    def getcursor1(self, ev):
        print('gettingcursor...')
        content = self.DBES_Employee_table2.item(self.DBES_Employee_table2.focus())
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
                self.upload_image_frame = Label(self.upload_image, image=self.Uploaded)
                self.upload_image_frame.place(x=280, y=162)

                self.Date.set(row[3])
                self.Employee_Salary.set(row[4])
                self.DBES_EOT.delete(0, END)
                self.DBES_EOT.insert(0, row[5])
                self.DBES_EGP.delete(0, END)
                self.DBES_EGP.insert(0, row[6])
                self.Employee_Income_Tax.set(row[7])
                self.DBES_ENP.delete(0, END)
                self.DBES_ENP.insert(0, row[8])
                self.DBES_save_btn['state'] = DISABLED
                self.DBES_EID['state'] = NORMAL
                self.DBES_EN['state'] = NORMAL
                self.DBES_ES['state'] = NORMAL
                self.DBES_EOT['state'] = NORMAL
                self.DBES_EIT['state'] = NORMAL
                self.DBES_Employee_Image['state'] = NORMAL
                self.DBES_EGP['state'] = NORMAL
                self.DBES_ENP['state'] = NORMAL

                self.DBES_cal_btn['state'] = NORMAL
                self.DBES_update_btn['state'] = NORMAL
                self.DBES_del_btn['state'] = NORMAL
                self.DVES_close_btn['state'] = NORMAL
            except Exception as e:
                messagebox.showerror("Error", f"Error{e}")
                print(f'Error')

    # -----| calculation |------
    def Calculate(self):
        print('calculate')
        if self.DBES_ES.get() == 'Amount':
            messagebox.showerror("Error", "Please Insert Amount")

        elif self.DBES_EOT.get() == 'Employee Over Time':
            e = messagebox.askquestion("Confirmation", "Do You Want to add Employee OverTIme")
            if e == 'yes':
                self.DBES_EOT.delete(0, END)
                self.DBES_EOT.focus()
                self.Overtime = self.Employee_Overtime
            else:
                self.DBES_EOT.delete(0, END)
                self.DBES_EOT.insert(0, 0)

        elif self.DBES_EIT.get() == 'Employee Tax':
            messagebox.showerror("Error", "Please Enter Employee Tax")

        else:
            # ----| Claculatioon for Gross pay |----
            self.Overtime = float(self.DBES_EOT.get()) * 200
            self.GrossPay1 = self.Employee_Salary.get() + float(self.Overtime)
            self.DBES_EGP.delete(0, END)
            self.DBES_EGP.insert(0, self.GrossPay1)
            # ----| Claculatioon for Net pay |----
            self.GrossPay2 = self.GrossPay1 - self.Employee_Income_Tax.get()
            self.DBES_ENP.delete(0, END)
            self.DBES_ENP.insert(0, self.GrossPay2)

            self.DBES_save_btn['state'] = NORMAL

    # ------| Save Function |-------
    def Save(self):
        print('Saving...')
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

        self.table = "Daily_Base_Employee_Salary"

        # Asking user to enter database name he wants to check
        # database_name = input('Enter database name to check exist or not: ')
        cur = conn.cursor()
        cur.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?;", (self.table,))
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
                '''Create table Daily_Base_Employee_Salary(
                    Salary_ID int Identity(1,1),
                    Employee_ID int,
                    Date date,
                    Amount int,
                    Employee_Over_Time float,
                    Gross_Pay float,
                    Tax int,
                    Net_Pay float
                    Constraint PK_Daily_Base_Employee_Salary Primary Key (Salary_ID)
                    FOREIGN KEY (Employee_ID) REFERENCES DBES_EI(Employee_ID)
                    )'''
            )
            print(" '{}' table Successfully Create in Payroll_Management Database".format(self.table))
        else:
            print(" '{}' table Exist in Payroll_Management Database".format(self.table))
            try:
                connect = pyodbc.connect(
                    "Driver={SQL Server};"
                    "Server=DESKTOP-SK0J9LF;"
                    "Database=Payroll_Management;"
                    "Trusted_Connection=yes;"
                )
                connect.autocommit = True

                cursor = connect.cursor()

                self.records = [self.Employee_id.get(), self.Date.get(), self.Employee_Salary.get(),
                                self.DBES_EOT.get(), self.DBES_EGP.get(), self.DBES_EIT.get(), self.DBES_ENP.get()]
                self.insert_query = "Insert into Daily_Base_Employee_Salary(Employee_ID, Date, Amount, Employee_Over_Time, Gross_Pay, Tax, Net_Pay) Values (?, ?, ?, ?, ?, ?, ?);"
                cursor.execute(self.insert_query, self.records)
                # go()
                connect.commit()
                connect.close()
                self.fetchdata()
                messagebox.showinfo("Information", "Record Updated Successfully( ' * ' )")
                self.clear()
                self.DBES_save_btn['state'] = DISABLED
                self.DBES_EID['state'] = DISABLED
                self.DBES_EN['state'] = DISABLED
                self.DBES_ES['state'] = DISABLED
                self.DBES_EOT['state'] = DISABLED
                self.DBES_EIT['state'] = DISABLED
                self.DBES_Employee_Image['state'] = DISABLED
                self.DBES_EGP['state'] = DISABLED
                self.DBES_ENP['state'] = DISABLED
            except Exception as e:
                print(f"Error {e}")
                messagebox.showerror("Error", f"Error {e}")

    def fetchdata(self):
        print('fetching...')
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
            Select e.Employee_ID, e.Employee_Name,e.Employee_Image, s.Date, s.Amount, s.Employee_Over_Time, s.Gross_Pay, s.Tax, s.Net_Pay from Daily_Base_Employee_Salary s join DBES_EI e on s.Employee_ID = e.Employee_ID
            and Date = ?
            order by Employee_ID;
            ''', (self.Date.get()))
        rows = cursor.fetchall()
        if not rows:
            print("No data in database!")
        elif len(rows) != 0:
            self.DBES_Employee_table2.delete(*self.DBES_Employee_table2.get_children())
            for row in rows:
                self.DBES_Employee_table2.insert('', END, text="", value=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
            connect.autocommit = True
        connect.close()

    def update(self):
        print('Update')
        try:

            connect = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=DESKTOP-SK0J9LF;"
                "Database=Payroll_Management;"
                "Trusted_Connection=yes;"
            )
            connect.autocommit = True

            cursor = connect.cursor()

            cursor.execute(
                "Update Payroll_Management.dbo.Daily_Base_Employee_Salary set Date = ?, Amount = ?, Employee_Over_Time = ?, Gross_Pay = ?, Tax = ?, Net_Pay = ? where Employee_ID = ?",
                (
                    self.Date.get(),
                    self.Employee_Salary.get(),
                    self.DBES_EOT.get(),
                    self.DBES_EGP.get(),
                    self.DBES_EIT.get(),
                    self.DBES_ENP.get(),
                    self.Employee_id.get()
                )
            )
            # go()
            connect.commit()
            connect.close()
            self.DBES_Employee_table2.delete(*self.DBES_Employee_table2.get_children())
            self.fetchdata()
            messagebox.showinfo("Information", "Record Updated Successfully( ' * ' )")
            self.clear()
            self.DBES_update_btn['state'] = DISABLED
            self.DBES_EID['state'] = DISABLED
            self.DBES_EN['state'] = DISABLED
            self.DBES_ES['state'] = DISABLED
            self.DBES_EOT['state'] = DISABLED
            self.DBES_EIT['state'] = DISABLED
            self.DBES_Employee_Image['state'] = DISABLED
            self.DBES_EGP['state'] = DISABLED
            self.DBES_ENP['state'] = DISABLED
        except Exception as e:
            print('Error', f'Error{e}')
            messagebox.showerror("Error", f"Error{e}")

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
            "Delete from Payroll_Management.dbo.Daily_Base_Employee_Salary where Employee_ID = ?",
            (
                self.Employee_id.get()
            )
        )
        # go()
        connect.commit()
        connect.close()
        self.DBES_Employee_table2.delete(*self.DBES_Employee_table2.get_children())
        self.fetchdata()
        messagebox.showinfo("Information", "Record Updated Successfully( ' * ' )")
        self.clear()
        self.DBES_EID['state'] = DISABLED
        self.DBES_EN['state'] = DISABLED
        self.DBES_ES['state'] = DISABLED
        self.DBES_EOT['state'] = DISABLED
        self.DBES_EIT['state'] = DISABLED
        self.DBES_Employee_Image['state'] = DISABLED
        self.DBES_EGP['state'] = DISABLED
        self.DBES_ENP['state'] = DISABLED
        self.DBES_del_btn['state'] = DISABLED
        self.DBES_update_btn['state'] = DISABLED

    def clear(self):

        self.DBES_EID.delete(0, END)
        self.DBES_EID.insert(0, 'Employee ID')

        self.DBES_EN.delete(0, END)
        self.DBES_EN.insert(0, 'Employee Name')

        self.DBES_ES.delete(0, END)
        self.DBES_ES.insert(0, 'Amount')

        self.DBES_Employee_Image.delete(0, END)
        self.DBES_Employee_Image.insert(0, 'Employee Image')

        self.DBES_EOT.delete(0, END)
        self.DBES_EOT.insert(0, 'Employee Over Time')

        self.DBES_EGP.delete(0, END)
        self.DBES_EGP.insert(0, 'Employee Gross Pay')

        self.DBES_EIT.delete(0, END)
        self.DBES_EIT.insert(0, 'Employee Tax')

        self.DBES_ENP.delete(0, END)
        self.DBES_ENP.insert(0, 'Employee Net Pay')

    def Create_Excel(self):
        print("Creating Excel...")
        # ---| Excel Sheet Creating start |---
        import pandas as pd

        data = [self.DBES_Employee_table2.item(item)['values'] for item in self.DBES_Employee_table2.get_children()]
        df = pd.DataFrame(data)
        df.to_csv('DailyBaseEmployeeSalary.CSV', encoding='shift-jis',
                  header=['Employee ID', 'Employee Name', 'Employee Image', 'Date', 'Amount', 'Absent', 'OverTime',
                          'Gross Pay', 'Employee Tax', 'Net Pay'], index=False)

        messagebox.showinfo("Information", "Successfully Generate Excel File")
#
# root = Tk()
# object = CDBES(root)
# root.mainloop()

