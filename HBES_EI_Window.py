from tkinter import *
from tkinter import ttk, IntVar
# from tkinter import tk
from tkinter import messagebox
from tkcalendar import DateEntry
import pyodbc
from time import sleep
from PIL import ImageTk, Image
from tkinter import filedialog
import pyodbc
# from setting import *
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
table_name = "HBES_EI"
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
        CREATE TABLE HBES_EI
               (
               Employee_ID int Identity (1,1) Not Null, 
               Joining_Date Date Not null,
               Employee_Name varchar(255) Not Null,
               Gmail varchar(255) Not Null,
               Phone_Number bigint Not Null,
               CNIC bigint Not Null,
               City varchar(50) Not Null,
               Gender varchar(10) Not Null,
               Age Int Not Null,
               Full_Address varchar(255) Not Null,
               Image_Path nvarchar(255) Not Null,
			   Constraint PK_HBES_EI Primary Key (Employee_ID)
               )
        '''
    )
    print(" '{}' table Successfully Create in Payroll_Management Database".format(table_name))
else:
    print(" '{}' table Exist in Payroll_Managemment Database".format(table_name))


class NewEmployee:
    NE_Employee_ID: IntVar

    # Uploaded = Uploaded
    def __init__(self, New_Employee):
        # self.Employee_ID = Employee_ID
        self.New_Employee = New_Employee
        self.New_Employee.title('Hourly Base Employee Salary')
        # self.New_Employee.geometry('1360x768+0+0')
        self.New_Employee.attributes("-fullscreen", True)
        self.New_Employee.resizable(0, 0)

        title = Label(self.New_Employee, text="HbEs AdD NeW EmPlOyeE", bd=4, font=("times new roman", 40), bg="#2e5cbe",
                      fg="black", relief=GROOVE, justify=CENTER)
        title.pack(side=TOP, fill=X)
        # _| Manage Frame |__
        self.NE_Manage_Frame = Frame(self.New_Employee, bd=4, relief=RIDGE, bg="#2e5cbe")
        self.NE_Manage_Frame.place(x=20, y=100, width=500, height=580)

        # _| Function for Entry placeholder removing |_

        def click1(*args):
            self.NE_EN.focus()
            if self.NE_Employee_name.get() == "Employee Name":
                self.NE_EN.delete(0, 'end')
                self.NE_EN.focus()

        def click2(*args):
            self.NE_E.focus()
            if self.NE_Email.get() == "XXXX@gmail.com":
                self.NE_E.delete(0, 'end')
                self.NE_E.focus()

        def click3(*args):
            # if self.NE_Contact.get() == '923000000000':
            self.NE_C.delete(0, 'end')

        def click4(*args):
            # if self.NE_CNIC.get() == "0000000000000":
            self.NE_nic.delete(0, 'end')

        def click5(*args):
            if self.NE_Age.get() == "Enter AGE":
                self.NE_Age.delete(0, END)
            # _| leave Function |__

        def leave(*args):
            self.NE_Manage_Frame.focus()

            if self.NE_Employee_name.get() == "":
                self.NE_EN.insert(0, 'Employee Name')
                self.NE_Manage_Frame.focus()
            elif self.NE_Email.get() == "":
                self.NE_E.insert(0, 'XXXX@gmail.com')
                self.NE_Manage_Frame.focus()
            elif self.NE_C.get() == "":
                self.NE_C.insert(0, '923000000000')
                self.NE_Manage_Frame.focus()
            elif self.NE_nic.get() == "":
                self.NE_nic.insert(0, '0000000000000')
                self.NE_Manage_Frame.focus()
            elif self.NE_Age.get() == "":
                self.NE_Age.insert(0, "Enter AGE")

        # -----} All Variable {-----
        self.NE_Employee_ID = IntVar()
        self.Date = StringVar()
        self.NE_Employee_name = StringVar()
        self.NE_Email = StringVar()
        self.NE_Contact = IntVar()
        self.NE_CNIC = IntVar()
        self.menu = StringVar()
        self.menu1 = StringVar()
        self.NE_Search_ID = IntVar()
        self.NE_Search_name = StringVar()
        self.NE_AGE = IntVar()
        self.imgpath = StringVar()

        # ______| Upload Image |_______
        def click6(*args):
            messagebox.showwarning("Warning", "On Select Image Path Auto set in this Entry Box\n Don't try to Enter")
            return "break"

        self.upload_image = Frame(self.NE_Manage_Frame, width=200, height=200).place(x=270, y=20)

        self.NE_img_path = Entry(self.NE_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                                 textvariable=self.imgpath)
        self.NE_img_path.place(x=270, y=240)
        self.NE_img_path.insert(0, 'Image Path')
        self.NE_img_path.bind("<Button-1>", click6)
        Button(self.NE_Manage_Frame, text='UPLOAD IMAGE', width=15, font=("times new roman", 10, "bold"), relief=GROOVE,
               bd=4, bg='teal', fg='oldlace', command=self.NE_upload_Image).place(x=307, y=300)

        # notallow bind funciton
        def notallow(*args):
            messagebox.showinfo("Info", "Please Don't Insert Employee ID\nBecause Employee ID Auto Generate!")
            return "break"

        self.NE_Employee_ID = IntVar()
        self.NE_EID = Entry(self.NE_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                            textvariable=self.NE_Employee_ID)

        self.NE_EID.place(x=20, y=10)
        self.NE_EID.delete(0, END)
        self.NE_EID.insert(0, 'Auto Employee ID')
        self.NE_EID.bind("<Button-1>", notallow)
        # self.NE_EID['state'] = DISABLED
        # #___ | Date Pciker | ____
        Label(self.NE_Manage_Frame, text="Date: ", bg="#2e5cbe", fg="black",
              font=("times new roman", 20, "bold")).place(x=20, y=60)
        cal = DateEntry(self.NE_Manage_Frame, textvariable=self.Date, width=10, year=2021, month=1, day=1,
                        background='darkblue', foreground='black', borderwidth=2, font=("times new roman", 15, "bold"))
        # self.Manage_Frame.focus()
        cal.place(x=100, y=65)

        # _| Entry Box Start |__

        # _| EN = Employee Name (Entry Box) |_
        self.NE_EN = Entry(self.NE_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                           textvariable=self.NE_Employee_name)

        # Add text in Entry box
        self.NE_EN.insert(0, 'Employee Name')
        self.NE_EN.place(x=20, y=120)

        # Use bind method
        self.NE_EN.bind("<Enter>", click1)
        self.NE_EN.bind("<Leave>", leave)
        # _| NE_E = EMAIL (Entry Box) |__
        self.NE_E = Entry(self.NE_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                          textvariable=self.NE_Email)
        # Add text in Entry box
        self.NE_E.insert(0, 'XXXX@gmail.com')
        self.NE_E.place(x=20, y=180)

        # Use bind method
        self.NE_E.bind("<Enter>", click2)
        self.NE_E.bind("<Leave>", leave)

        # -----} Contact function {-----
        def only_allow_numbers1(event):
            char = event.char.lower()
            if (event.state & 4) >> 2:
                return None

            if char.isprintable() and (not event.char.isdigit()):
                messagebox.showerror("Error", "String Not Allow\nPlease Enter Number")
                return "break"
            elif len(self.NE_C.get()) > 11:
                messagebox.showerror("Error", "Phone Number has limit 12 digit like this 923XXXXXXXXX")
                self.New_Employee.focus()
                self.NE_nic.focus()
                return "break"

        # ----} Contact {----
        self.NE_C = Entry(self.NE_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                          textvariable=self.NE_Contact)
        self.NE_C.insert(0, '92300000000')
        self.NE_C.place(x=20, y=240)
        # use Bind method
        self.NE_C.bind("<Button-1>", click3)
        self.NE_C.bind("<Leave>", leave)
        self.NE_C.bind("<Key>", only_allow_numbers1)

        def only_allow_nicnumbers(event):
            char = event.char.lower()
            if (event.state & 3) >> 2:
                return None

            if char.isprintable() and (not event.char.isdigit()):
                messagebox.showerror("Error", "String Not Allow\nPlease Enter Number")
                return "break"
            elif len(self.NE_nic.get()) > 12:
                messagebox.showerror("Error", "Please Enter CNIC Number Like this 00000000000000")
                self.New_Employee.focus()
                # self.NE_nic.focus()
                return "break"

        # _| EOT = CNIC (Entry Box) |___

        self.NE_nic = Entry(self.NE_Manage_Frame, bd=4, width=20, font=("times new roman", 15),
                            textvariable=self.NE_CNIC)
        # Add text in Entry box
        self.NE_nic.insert(0, '000000000000')
        self.NE_nic.place(x=20, y=300)
        # bind
        self.NE_nic.bind("<Button-1>", click4)
        self.NE_nic.bind("<Leave>", leave)
        self.NE_nic.bind("<Key>", only_allow_nicnumbers)

        # -----} City {------
        self.menu = StringVar()
        self.menu.set("Select City")

        # Create a dropdown Menu
        self.drop = OptionMenu(self.NE_Manage_Frame, self.menu, 'Karachi', 'Sindh', 'Lahore', 'Punjab', 'Islamabad',
                               'Peshawur')
        self.drop.place(x=20, y=362, width=120)

        # -----} Gender {------
        self.menu1 = StringVar()
        self.menu1.set("Select Gender")

        # Create a dropdown Menu
        self.drop = OptionMenu(self.NE_Manage_Frame, self.menu1, 'Male', 'Female', 'Others')
        self.drop.place(x=160, y=362, width=120)

        # ---} Employee Age {----
        self.NE_Age = Entry(self.NE_Manage_Frame, bd=4, width=15, font=("times new roman", 15),
                            textvariable=self.NE_AGE)
        self.NE_Age.place(x=300, y=362)
        self.NE_Age.delete(0, END)
        self.NE_Age.insert(0, "Enter AGE")
        self.NE_Age.bind("<Enter>", click5)
        self.NE_Age.bind("<Leave>", leave)

        # 6
        Label(self.NE_Manage_Frame, text="Full Address", font=("times new roman", 16, "bold"), bg="#2e5cbe",
              fg='black').place(x=20, y=400)
        self.NE_Address = Text(self.NE_Manage_Frame, width=55, height=2)
        self.NE_Address.place(x=20, y=430)

        # __ | Entry Box End | __
        # __| Button |__

        self.NE_submit_btn = Button(self.NE_Manage_Frame, text="SUBMIT", width=15, font=("times new roman", 10, "bold"),
                                    relief=GROOVE, bd=4, bg='maroon', fg='oldlace', command=self.submit)
        self.NE_submit_btn.place(x=50, y=480)

        self.delete_btn = Button(self.NE_Manage_Frame, text="Delete", width=15, font=("times new roman", 10, "bold"),
                                 relief=GROOVE, bd=4,
                                 bg='red', fg='white', command=self.delete)
        self.delete_btn.place(x=180, y=480)
        self.delete_btn['state'] = DISABLED

        self.update_btn = Button(self.NE_Manage_Frame, text="UPDATE", width=15, font=("times new roman", 10, "bold"),
                                 relief=GROOVE, bd=4,
                                 bg='mistyrose', fg='black', command=self.update)
        self.update_btn.place(x=310, y=480)
        self.update_btn['state'] = DISABLED

        self.bacnk_btn = Button(self.NE_Manage_Frame, text="Back", width=15, font=("times new roman", 10, "bold"),
                                relief=GROOVE, bd=4,
                                bg='royalblue', fg='black')
        self.bacnk_btn.place(x=180, y=530)

        Button(self.NE_Manage_Frame, text="Close", width=15, height=1, font=("times new roman", 10, "bold"),
               relief=GROOVE, bd=4,
               bg='aliceblue', fg='crimson', command=lambda: exit()).place(x=310, y=530)

        self.clear_btn = Button(self.NE_Manage_Frame, text="Clear", width=15, font=("times new roman", 10, "bold"),
                                relief=GROOVE, bd=4,
                                bg='palegreen', fg='black', command=self.clear).place(x=50, y=530)

        # _| Detail Frame |__
        self.NE_Detail_Frame = Frame(New_Employee, bd=4, relief=RIDGE, bg="#2e5cbe")
        self.NE_Detail_Frame.place(x=545, y=100, width=800, height=580)

        lbl_search = Label(self.NE_Detail_Frame, text="Search By", bg="#2e5cbe", fg="black",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        # -----} Serch Enter ID binding function {------
        def NE_Search_ID(*args):
            if self.NE_Search_Id.get() == 'Enter ID':
                self.NE_Search_Id.delete(0, END)
                self.NE_Search_Id.focus()

        def leave1(*args):
            self.NE_Detail_Frame.focus()
            if self.NE_Search_Id.get() == "" or self.NE_Search_Id.get() == 'Enter ID':
                self.NE_Search_Id.insert(0, 'Enter ID')
                self.NE_Detail_Frame.focus()

        def NE_Search_Id(*args):
            connect = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=DESKTOP-SK0J9LF;"
                "Database=Payroll_Management;"
                "Trusted_Connection=yes;"
            )
            connect.autocommit = True

            cursor = connect.cursor()

            cursor.execute(
                "select * from Payroll_Management.dbo.HBES_EI where Employee_ID Like '%" +
                str(self.NE_Search_Id.get()) + "%'")
            rows = cursor.fetchall()
            if not rows:
                self.NE_Employee_table.delete(*self.NE_Employee_table.get_children())
                messagebox.showerror("Error", "No data to display")
                print("No data in database!")
            elif len(rows) != 0:
                self.NE_Employee_table.delete(*self.NE_Employee_table.get_children())
                for row in rows:
                    self.NE_Employee_table.insert('', END, text="", value=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                connect.autocommit = True
            connect.close()

        # ----| binding function end |----
        # ------} Search Entery {--------
        self.NE_Search_Id = Entry(self.NE_Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                  relief=GROOVE, textvariable=self.NE_Search_ID)
        self.NE_Search_Id.grid(row=0, column=1, padx=20, pady=10, sticky=W)
        self.NE_Search_Id.delete(0, END)
        self.NE_Search_Id.insert(0, 'Enter ID')
        self.NE_Search_Id.bind("<Enter>", NE_Search_ID)
        self.NE_Search_Id.bind("<KeyRelease>", NE_Search_Id)
        self.NE_Search_Id.bind("<Leave>", leave1)

        # ------} Search Enter Name {-------
        def NE_search_name(*args):
            data = self.NE_Search_name.get()
            if self.NE_Search_Name.get() == 'Enter Name' or self.NE_Search_name.get() == "":
                self.NE_Search_Name.delete(0, END)
                self.NE_Search_Name.focus()

        def leave2(*args):
            if self.NE_Search_Name.get() == "" or self.NE_Search_Name.get() == 'Enter Name':
                self.NE_Search_Name.insert(0, 'Enter Name')
                self.NE_Detail_Frame.focus()
                # self.NE_Manage_Frame.focus()

        def search(*args):
            connect = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=DESKTOP-SK0J9LF;"
                "Database=Payroll_Management;"
                "Trusted_Connection=yes;"
            )
            connect.autocommit = True

            cursor = connect.cursor()

            cursor.execute(
                "select * from Payroll_Management.dbo.HBES_EI where Employee_Name Like '%" + str(
                    self.NE_Search_name.get()) + "%'")
            rows = cursor.fetchall()
            if not rows:
                print("No data in database!")
            elif len(rows) != 0:
                self.NE_Employee_table.delete(*self.NE_Employee_table.get_children())
                for row in rows:
                    self.NE_Employee_table.insert('', END, text="", value=(
                        row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
                connect.autocommit = True
            connect.close()

        # ----} End Binding function with Search Enter Name {-----

        # ------} Search Entery {--------
        self.NE_Search_Name = Entry(self.NE_Detail_Frame, width=15, font=("times new roman", 13, "bold"), bd=5,
                                    relief=GROOVE, textvariable=self.NE_Search_name)
        self.NE_Search_Name.grid(row=0, column=2)
        self.NE_Search_Name.insert(0, 'Enter Name')
        self.NE_Search_Name.bind("<Enter>", NE_search_name)
        self.NE_Search_Name.bind("<KeyRelease>", search)
        self.NE_Search_Name.bind("<Leave>", leave2)

        # search_btn = Button(self.NE_Detail_Frame, text="Search", width=15, command=self.NE_Search)
        # search_btn.grid(row=0, column=3, padx=20, pady=10)

        self.NE_Table_Frame = Frame(self.NE_Detail_Frame, bd=4, relief=RIDGE, bg="white")
        self.NE_Table_Frame.place(x=10, y=50, width=760, height=500)

        # scrollbar = Scrollbar(Table_Frame,orient=VERTICAL)
        # scrollbar.grid(row=1,cloumn=2,sticky=N+S)
        # Table_Frame.configure(yscrollcommand=scrollbar.set)

        self.NE_scroll_x = Scrollbar(self.NE_Table_Frame, orient=HORIZONTAL)
        self.NE_scroll_y = Scrollbar(self.NE_Table_Frame, orient=VERTICAL)
        self.NE_Employee_table = ttk.Treeview(self.NE_Table_Frame, columns=(
            "Employee_ID", "Joining_Date", "Employee_Name", "Gmail", "Phone_Number",
            "CNIC", "City", "Gender", "Employee_Age", "Full_Address", "Employee_Image"),
                                              xscrollcommand=self.NE_scroll_x.set,
                                              yscrollcommand=self.NE_scroll_y.set)
        self.NE_scroll_x.pack(side=BOTTOM, fill=X)
        self.NE_scroll_y.pack(side=RIGHT, fill=Y)
        self.NE_scroll_x.configure(command=self.NE_Employee_table.xview)
        self.NE_scroll_y.configure(command=self.NE_Employee_table.yview)
        self.NE_Employee_table.heading("Employee_ID", text="Employee ID")
        self.NE_Employee_table.heading("Joining_Date", text="Joining Date")
        self.NE_Employee_table.heading("Employee_Name", text="Employee Name")
        self.NE_Employee_table.heading("Gmail", text="Gmail")
        self.NE_Employee_table.heading("Phone_Number", text="Contact Number")
        self.NE_Employee_table.heading("CNIC", text="CNIC")
        self.NE_Employee_table.heading("City", text="City")
        self.NE_Employee_table.heading("Gender", text="Gender")
        self.NE_Employee_table.heading("Employee_Age", text="Age")
        self.NE_Employee_table.heading("Full_Address", text="Full Address")
        self.NE_Employee_table.heading("Employee_Image", text="Employee Image")
        self.NE_Employee_table['show'] = 'headings'
        # self.NE_Employee_table.heading("Employee_Image", text="Employee Image")
        # ----| Grid Table Column sizing |-----
        self.NE_Employee_table.column("Employee_ID", width=100)
        self.NE_Employee_table.column("Joining_Date", width=100)
        self.NE_Employee_table.column("CNIC", width=100)
        self.NE_Employee_table.column("City", width=100)
        self.NE_Employee_table.column("Gender", width=100)
        self.NE_Employee_table.column("Employee_Age", width=100)
        self.NE_Employee_table.column("Full_Address", width=400)
        self.NE_Employee_table.column("Employee_Image", width=300)
        self.NE_Employee_table.pack(fill=BOTH, expand=1)

        # -----} Binding Table {-------
        self.NE_Employee_table.bind("<ButtonRelease-1>", self.getcursor)
        # -----} Fetcihng Data {-------
        self.fetchdata()

    def NE_upload_Image(self, *args):
        global Uploaded
        try:
            self.upload = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(
                ("PNG files", "*.png"), ("jpeg files", "*.jpg"), ("jpng files", "*.jpng")))

            self.Uploaded = ImageTk.PhotoImage(Image.open(self.upload))
            if self.Uploaded.width() == 192 or self.Uploaded.height() == 192:
                self.img_lbl = Label(self.upload_image, image=self.Uploaded, width=192, height=192, bg="white")
                self.img_lbl.place(x=296, y=126)
                self.NE_img_path.delete(0, END)
                self.NE_img_path.insert(0, self.upload)
                print(self.upload)
            else:
                messagebox.showerror("error", 'image size should 192x192')
        except:
            print("error")

    # ------} Submit Function {-------
    def submit(self, *args):

        if self.NE_Employee_name.get() == 'Employee Name' or self.NE_Employee_name.get() == "":
            messagebox.showerror("Error", "Please Enter Employee Name")

        elif self.NE_Email.get() == 'XXXX@gmail.com' or self.NE_Email.get() == "":
            messagebox.showerror("Error", "Please Enter EMAIL")

        elif self.NE_C.get() == '923000000000' or self.NE_C.get() == "":
            messagebox.showerror("Error", "Please Enter Employee Contact Number")

        elif self.NE_nic.get() == '0000000000000' or self.NE_nic.get() == "":
            messagebox.showerror("Error", "Pelease Enter CNIC Number")

        elif self.menu.get() == "Select City" or self.menu.get() == "":
            messagebox.showerror("Error", "Please Select City")

        elif self.menu1.get() == "Select Gender" or self.menu1.get() == "":
            messagebox.showerror("Error", "Please Select Gender")

        elif self.NE_Age.get() == "Enter AGE" or self.NE_Age.get() == "":
            messagebox.showerror("Error", "Please Enter AGE")

        elif len(self.NE_Address.get("1.0", "end-1c")) == 0:
            messagebox.showerror("Error", "Please Enter Your Full Address")


        else:
            connect = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=DESKTOP-SK0J9LF;"
                "Database=Payroll_Management;"
                "Trusted_Connection=yes;"
            )
            connect.autocommit = True

            cursor = connect.cursor()
            cursor.execute('''
                SELECT DBES_EI.Employee_Name, HBES_EI.Employee_Name, MBES_EI.Employee_Name
                    FROM DBES_EI,HBES_EI,MBES_EI
                    WHERE DBES_EI.Employee_Name = ?
                    OR HBES_EI.Employee_Name = ?
                    OR MBES_EI.Employee_Name =?
            ''',(self.NE_Employee_name.get(),self.NE_Employee_name.get(),self.NE_Employee_name.get(),))
            data = cursor.fetchall()
            if not data:
                self.records = [self.Date.get(), self.NE_Employee_name.get(), self.NE_Email.get(),
                                self.NE_Contact.get(), self.NE_CNIC.get(), self.menu.get(), self.menu1.get(),
                                self.NE_Age.get(),
                                self.NE_Address.get("1.0", "end-1c"), self.NE_img_path.get()]
                self.insert_query = "Insert into HBES_EI(Joining_Date,Employee_Name,Gmail,Phone_Number,CNIC,City,Gender,Age,Full_Address,Image_Path) Values (? ,?, ?, ?, ?, ?, ?, ?, ?, ?);"
                cursor.execute(self.insert_query, self.records)
                connect.commit()
                self.fetchdata()
                connect.close()
                print(" '{}' Values Insert Successfully: ")

                print("Date: " + self.Date.get())
                print("Employee Name: " + self.NE_Employee_name.get())
                print("EMAIL: " + self.NE_Email.get())
                print("Contact N0: " + self.NE_C.get())
                print("CNINC: " + self.NE_nic.get())
                print("City: " + self.menu.get())
                print("Gender: " + self.menu1.get())
                print("Full Address: " + self.NE_Address.get("1.0", "end-1c"))

                self.clear()
                messagebox.showinfo("Information", "Record Save Successfully (' : ')")
            else:
                messagebox.showerror("Error","Record Exists in 'Payroll_Management' Database! ")
                self.clear()
    # ------} Clear Functuion {-------
    # ----} Clear button {-----
    def clear(self):
        self.delete_btn['state'] = DISABLED
        self.update_btn['state'] = DISABLED
        self.NE_submit_btn['state'] = NORMAL
        self.NE_EID.delete(0, 'end')
        self.NE_EID.insert(0, 'Auto Employee ID')
        self.NE_EN.delete(0, 'end')
        self.NE_EN.insert(0, 'Employee Name')

        # _| Rate |__
        self.NE_E.delete(0, 'end')
        self.NE_E.insert(0, 'XXXX@gmail.com')
        # _| Hour |_
        self.NE_C.delete(0, 'end')
        self.NE_C.insert(0, '923000000000')
        # _| OVer Time |_
        self.NE_nic.delete(0, 'end')
        self.NE_nic.insert(0, '0000000000000')
        # _| City |_
        self.menu.set("Select City")
        # -| Gender |_
        self.menu1.set("Select Gender")
        # _| Age _|
        self.NE_Age.delete(0, END)
        self.NE_Age.insert(0, 'Enter AGE')
        # _| Full Address |_
        self.NE_Address.delete(1.0, 'end')

        self.Date.set('1/1/21')

        self.NE_img_path.delete(0, END)
        self.NE_img_path.insert(0,'Image Path')
        self.upload_image = Frame(self.upload_image, width=200, height=200, bg='black').place(x=294, y=124)

        self.NE_Manage_Frame.focus()

    # -------} Fetch Data {-------
    def fetchdata(self):
        connect = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-SK0J9LF;"
            "Database=Payroll_Management;"
            "Trusted_Connection=yes;"
        )
        connect.autocommit = True

        cursor = connect.cursor()

        cursor.execute("select * from HBES_EI")
        rows = cursor.fetchall()
        if not rows:
            print("No data in database!")
        elif len(rows) != 0:
            self.NE_Employee_table.delete(*self.NE_Employee_table.get_children())
            for row in rows:
                self.NE_Employee_table.insert('', END, text="", value=(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
            connect.autocommit = True
        connect.close()

    # -------} Get Cursor {-------
    def getcursor(self, ev):
        self.delete_btn['state'] = NORMAL
        self.update_btn['state'] = NORMAL
        self.NE_submit_btn['state'] = DISABLED
        # cursor_row = self.NE_Employee_table.focus()

        content = self.NE_Employee_table.item(self.NE_Employee_table.focus())

        row = content['values']
        if not row:
            print("Just Row Select")
        else:
            print(row)
            self.NE_Employee_ID.set(row[0])
            self.Date.set(row[1])
            self.NE_Employee_name.set(row[2])
            self.NE_Email.set(row[3])
            self.NE_Contact.set(row[4])
            self.NE_CNIC.set(row[5])
            self.menu.set(row[6])
            self.menu1.set(row[7])
            self.NE_AGE.set(row[8])
            self.NE_Address.delete("1.0", "end-1c")
            self.NE_Address.insert(END, row[9])

            # ----} Image Code {-----
            self.imgpath.set(row[10])
            lblimg = self.imgpath.get()
            try:
                print(lblimg)
                self.image = ImageTk.PhotoImage(Image.open(lblimg))
                # self.ig = ImageTk.PhotoImage(self.image)
                self.imageLabel = Label(self.upload_image, image=self.image, width=192, height=192, bg="white")
                self.imageLabel.place(x=296, y=126)
            except:
                messagebox.showerror("Error", "No Such File or Directory")
                print("No Such File or directory")

    # -----} Update {------
    def update(self):
        if self.NE_Employee_name.get() == 'Employee Name' or self.NE_Employee_name.get() == "":
            messagebox.showerror("Error", "Please Enter Employee Name")

        elif self.NE_Email.get() == 'XXXX@gmail.com' or self.NE_Email.get() == "":
            messagebox.showerror("Error", "Please Enter EMAIL")

        elif self.NE_C.get() == '923000000000' or self.NE_C.get() == "":
            messagebox.showerror("Error", "Please Enter Employee Contact Number")

        elif self.NE_nic.get() == '0000000000000' or self.NE_nic.get() == "":
            messagebox.showerror("Error", "Pelease Enter CNIC Number")

        elif self.menu.get() == "Select City" or self.menu.get() == "":
            messagebox.showerror("Error", "Please Select City")

        elif self.menu1.get() == "Select Gender" or self.menu1.get() == "":
            messagebox.showerror("Error", "Please Select Gender")

        elif len(self.NE_Address.get("1.0", "end-1c")) == 0:
            messagebox.showerror("Error", "Please Enter Your Full Address")
        else:
            print('Update button click')
            self.NE_submit_btn['state'] = NORMAL

            connect = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=DESKTOP-SK0J9LF;"
                "Database=Payroll_Management;"
                "Trusted_Connection=yes;"
            )
            connect.autocommit = True

            cursor = connect.cursor()

            cursor.execute(
                "update Payroll_Management.dbo.HBES_EI SET Joining_Date = ?, Employee_Name = ?, Gmail = ?, Phone_Number = ?, CNIC = ?, City = ?, Gender = ?, Age = ?, Full_Address = ?, Image_Path = ? where Employee_ID = ?",
                (
                    self.Date.get(),
                    self.NE_Employee_name.get(),
                    self.NE_Email.get(),
                    self.NE_Contact.get(),
                    self.NE_CNIC.get(),
                    self.menu.get(),
                    self.menu1.get(),
                    self.NE_AGE.get(),
                    self.NE_Address.get("1.0", "end-1c"),
                    self.NE_img_path.get(),
                    self.NE_Employee_ID.get(),
                ))
            connect.commit()
            self.fetchdata()
            self.clear()
            messagebox.showinfo("Information", "Record Updated Successfully!")
            connect.close()

    # -------} Delete {-------
    def delete(self):
        MsgBox = messagebox.askquestion('Exit Application', 'Are You Sure You Want to delete this record!',
                                        icon='warning')
        if MsgBox == 'yes':
            connect = pyodbc.connect(
                "Driver={SQL Server};"
                "Server=DESKTOP-SK0J9LF;"
                "Database=Payroll_Management;"
                "Trusted_Connection=yes;"
            )
            connect.autocommit = True

            cursor = connect.cursor()

            cursor.execute(
                "delete from Payroll_Management.dbo.HBES_EI  where Employee_ID = ?",
                (
                    self.NE_Employee_ID.get(),
                ))
            connect.commit()
            self.fetchdata()
            self.clear()
            messagebox.showinfo("Info", "Record Deleted Successfully (' : ')")
            connect.close()

# New_Employee = Tk()
# obj = NewEmployee(New_Employee)
# New_Employee.mainloop()
