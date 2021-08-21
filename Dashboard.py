from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime
from datetime import date
from setting import *
from HBES_Window import *
from DBES_Window import *
from MBES_WIndow import *


# ----} Multi Level Inheritance |------
class HbEs:
    def hBeS(self):
        root = Tk()
        obj = HBES(root)
        root.mainloop()


class DbEs(HbEs):
    def dBeS(self):
        root = Tk()
        object = CDBES(root)
        root.mainloop()


class MbEs(DbEs):
    def mBeS(self):
        root = Tk()
        obj = MBES(root)
        root.mainloop()


class SeTtInG(MbEs):
    def sEtTiNg(self):
        setting = Tk()
        obj2 = Setting(setting)
        setting.mainloop()


objs = SeTtInG()


class Dashboard_Window:
    # ______| Class Initializing |_____

    def __init__(self, dashboard_Window):
        self.dashboard_Window = dashboard_Window
        self.dashboard_Window.title("AAH Company")
        self.dashboard_Window.attributes("-fullscreen", True)
        self.dashboard_Window.configure(background="whitesmoke")
        self.dashboard_Window.resizable(0, 0)

        # _______| Employee Salary function Finish |________
        def Employee_Salary():
            # self.Second_Window.destroy()
            messagebox.showinfo("Info", "Please Wait because work in progress")

        # # ______| Label |_______
        title = Label(self.dashboard_Window, width=50, text="Welcome to Payroll Management System", bg="lightblue",
                      relief=GROOVE, justify=CENTER,
                      font=("Times", 30, "bold"), bd=6).pack(side=TOP, fill=X)
        # _____| LableFrame and Button in  LabelFrame |_____
        swlf1 = LabelFrame(self.dashboard_Window, text="AAH Company", font=30, fg="black", bg="whitesmoke",
                           width=220,
                           height=650).place(x=10, y=70)

        self.img_reg1 = ImageTk.PhotoImage(
            file=r"C:\images\i.jpg")
        self.btn_registration1 = Button(swlf1, text="Hourly base \n Employee Salary", width=180,
                                        image=self.img_reg1, compound="top", borderwidth=2,
                                        command=self.HourBaseES, bg="light blue",
                                        font=('times', 18, 'bold'), height=140)
        self.btn_registration1.place(x=20, y=100)

        self.img_reg2 = ImageTk.PhotoImage(
            file=r"C:\images\i.jpg")
        self.btn_registration2 = Button(swlf1, text="Daily Base \n Employee Salary", width=180,
                                        image=self.img_reg2, compound="top", borderwidth=2,
                                        command=self.DailyBaseES, bg="light blue",
                                        font=('times', 18, 'bold'), height=140)
        self.btn_registration2.place(x=20, y=250)

        self.img_reg4 = ImageTk.PhotoImage(file=r"C:\images\i.jpg")
        self.btn_registration4 = Button(swlf1, text="Monthly Base \n Employee Salary", width=180,
                                        image=self.img_reg4, compound="top", borderwidth=2,
                                        command=self.MonnthlyBaseES, bg="light blue",
                                        font=('times', 18, 'bold'), height=140)
        self.btn_registration4.place(x=20, y=400)

        self.img_reg5 = ImageTk.PhotoImage(
            file=r"C:\images\ii.jpg")
        self.btn_registration5 = Button(swlf1, text="Add New \n Employee", width=180,
                                        image=self.img_reg5, compound="top", borderwidth=2,
                                        command=self.setall, bg="light blue",
                                        font=('times', 18, 'bold'), height=140)
        self.btn_registration5.place(x=20, y=550)

        swlf2 = LabelFrame(self.dashboard_Window, font=30, fg="black", bg="whitesmoke", width=1000,
                           height=630).place(x=210, y=80)
        self.log = ImageTk.PhotoImage(file="C:/images/payroll.jfif")
        log = Label(swlf2, image=self.log).place(x=210, y=80, width=1000, height=630)

    def HourBaseES(self):
        self.dashboard_Window.destroy()
        objs.hBeS()

    def DailyBaseES(self):
        self.dashboard_Window.destroy()
        objs.dBeS()

    def MonnthlyBaseES(self):
        self.dashboard_Window.destroy()
        objs.mBeS()

    def setall(self):
        self.dashboard_Window.destroy()
        objs.sEtTiNg()


# dashboard_Window = Tk()
# obj = Dashboard_Window(dashboard_Window)
# dashboard_Window.mainloop()
# _________| Dashboard Window End |_______
