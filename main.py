from tkinter import *
from tkinter import ttk
import pyodbc
from abc import ABC, abstractmethod

connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
connect.autocommit = True

cursor = connect.cursor()
class Allownces1:
    @abstractmethod
    def allownces(self):
        pass


class Allownces2(Allownces1):
    def allownces(self):
        self.allownc = Tk()
        self.allownc.title('Employee Allownces')
        self.allownc.attributes("-fullscreen", True)
        self.title = Label(self.allownc, text="(--------} EMPLOYEE Allownces {--------)", bd=4,
                           font=("times new roman", 40), bg="navy",
                           fg="oldlace", relief=GROOVE, justify=CENTER)
        self.title.pack(side=TOP, fill=X)

        self.all_btn = Button(self.allownc, text='All Employee', width=15, font=("times new roman", 10, "bold"),
                              relief=GROOVE,
                              bd=4, bg='teal', fg='oldlace', command=self.allemp)
        self.all_btn.place(x=300, y=150)

        self.del_btn = Button(self.allownc, text='Delete', width=10, font=("times new roman", 10, "bold"),
                              relief=GROOVE,
                              bd=4, bg='teal', fg='oldlace')
        self.del_btn.place(x=450, y=150)

        self.all_btn = Button(self.allownc, text='Add Allownce', width=15, font=("times new roman", 10, "bold"),
                              relief=GROOVE,
                              bd=4, bg='teal', fg='oldlace',command=self.addallown)
        self.all_btn.place(x=550, y=150)

        self.close_btn = Button(self.allownc, text='Close', width=10, font=("times new roman", 10, "bold"),
                                relief=GROOVE,
                                bd=4, bg='red', fg='oldlace', command=lambda: exit())
        self.close_btn.place(x=970, y=100)

        def click1(*args):
            self.EID.delete(0, 'end')

        def leave1(*args):
            if self.EID.get() == "":
                self.EID.insert(0, 'Employee ID')
                self.Table_Frame2.focus()

        self.Employee_id = IntVar()
        self.EID = Entry(self.allownc, bd=4, width=15, font=("times new roman", 15), textvariable=self.Employee_id)

        # Add text in Entry box
        self.EID.place(x=700, y=150)
        self.EID.delete(0, END)
        self.EID.insert(0, 'Employee ID')
        self.EID.bind("<Button-1>", click1)
        self.EID.bind("<Leave>", leave1)

        def click2(*args):
            self.EN.delete(0, END)

        def leave2(*args):
            if self.Employee_name.get() == "":
                self.EN.insert(0, 'Employee Name')
                self.Table_Frame2.focus()

        self.Employee_name = StringVar()
        self.EN = Entry(self.allownc, bd=4, width=15, font=("times new roman", 15), textvariable=self.Employee_name)

        # Add text in Entry box
        self.EN.place(x=900, y=150)
        self.EN.insert(0, 'Employee Name')
        self.EN.bind("<Button-1>", click2)
        self.EN.bind("<Leave>", leave2)

        # -------| Table Frame Tree View |-------
        self.Table_Frame2 = Frame(self.allownc, bd=4, relief=RIDGE, bg="white")
        self.Table_Frame2.place(x=300, y=200, width=800, height=500)

        self.scroll_x = Scrollbar(self.Table_Frame2, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame2, orient=VERTICAL)
        self.Employee_table2 = ttk.Treeview(self.Table_Frame2, columns=(
            "Employee_ID", "Employee_Name", "Joining_Date", "Salary"), xscrollcommand=self.scroll_x.set,
                                            yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.configure(command=self.Employee_table2.xview)
        self.scroll_y.configure(command=self.Employee_table2.yview)
        self.Employee_table2.heading("Employee_ID", text="Employee ID")
        self.Employee_table2.heading("Employee_Name", text="Employee Name")
        self.Employee_table2.heading("Joining_Date", text="Joining Date")
        self.Employee_table2.heading("Salary", text="Salary")
        self.Employee_table2['show'] = 'headings'
        self.Employee_table2.column("Employee_ID", width=100)
        self.Employee_table2.pack(fill=BOTH, expand=1)
        # ------| Binding |------
        # self.Employee_table2.bind("<ButtonRelease-1>", self.getcursor1)
        self.allownc.mainloop()

    def allemp(self):
        print('All Employee...')
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True

        cursor = connect.cursor()

        cursor.execute('''
         Select e.Employee_ID, e.Employee_Name, e.Joining_Date, s.Amount from Monthly_Base_Employee_Salary s join MBES_EI e on s.Employee_ID = e.Employee_ID

        ''')
        rows = cursor.fetchall()
        if not rows:
            print("No data in database!")
        elif len(rows) != 0:
            self.Employee_table2.delete(*self.Employee_table2.get_children())
            for row in rows:
                self.Employee_table2.insert('', END, text="", value=(
                    row[0], row[1], row[2], row[3]))
            connect.autocommit = True
        connect.close()

    def addallown(self):
        data = [self.Employee_table2.item(item)['values'] for item in self.Employee_table2.get_children()]
        for i in data:
            id = i[0]
            print(id)


allownacesobj = Allownces2()
allownacesobj.allownces()
