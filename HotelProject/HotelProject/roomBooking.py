import RegisterMember
import datetime
from tkinter import *


class Booking:  # Uses the Member Class to Book a room

    def __init__(self, memberID=1001, password="password", age=0, email="@gmail.com", roomID=2202, city="Rome",
                 check_in=0, check_out=2, business=True, breakfast=False, NofA=0):
        self.RegisterObj = RegisterMember.Register(memberID, password, age, email)
        self.roomID = roomID
        self.city = city
        self.check_in = check_in
        self.check_out = check_out
        self.business = business
        self.breakfast = breakfast
        self.NofA = NofA

    def InputBooking(self):
        def Store():
            roomNumber = 0
            if Input1.get() != "":
                roomNumber = 1000 + int(Input1.get())
            elif Input2.get() != "":
                roomNumber = 2000 + int(Input2.get())
            elif Input3.get() != "":
                roomNumber = 3000 + int(Input3.get())
            self.roomID = str(roomNumber)

            self.city = Input2.get()

            month = int(Input3Month.get())
            day = int(Input3Day.get())
            self.check_in = datetime.date(2024, month, day)

            month = int(Input4Month.get())
            day = int(Input4Day.get())
            self.check_out = datetime.date(2024, month, day)

            if not isinstance(self.check_in, datetime.date):
                self.check_in = datetime.date(self.check_in.year, self.check_in.month, self.check_in.day)

            if not isinstance(self.check_out, datetime.date):
                self.check_out = datetime.date(self.check_out.year, self.check_out.month, self.check_out.day)



            if str(Input5.get()).lower() == "yes":
                self.business = True
            else:
                self.business = False

            if str(Input6.get()).lower() == "yes":
                self.breakfast = True
            else:
                self.breakfast = False

            self.NofA = int(Input7.get())

            SuccessLbl = Label(BottomFrame, text="Successfully Registered")
            SuccessLbl.pack()


        BookingGUI = Tk()
        BookingGUI.configure(bg="black")
        MainFrame = Frame(BookingGUI)
        MainFrame.pack(padx=10, pady=10)

        L1 = Label(MainFrame, text="Enter RoomID (4 digits)")
        L1.pack()
        Input1 = Entry(MainFrame)
        Input1.pack()

        L2 = Label(MainFrame, text="Enter city (Rome, Bolzano , Milan )")
        L2.pack()
        Input2 = Entry(MainFrame)
        Input2.pack()

        L3Month = Label(MainFrame, text="Enter check-in Month")
        L3Day = Label(MainFrame, text="Enter check-in Day")

        Input3Month = Entry(MainFrame)
        L3Month.pack()
        Input3Month.pack()
        Input3Day = Entry(MainFrame)
        L3Day.pack()
        Input3Day.pack()

        L4Month = Label(MainFrame, text="Enter check_Out Month")
        L4Day = Label(MainFrame, text="Enter check_Out Day")

        Input4Month = Entry(MainFrame)
        L4Month.pack()
        Input4Month.pack()
        Input4Day = Entry(MainFrame)
        L4Day.pack()
        Input4Day.pack()

        L5 = Label(MainFrame, text="Any Discounts Available(yes/no)")
        L5.pack()
        Input5 = Entry(MainFrame)
        Input5.pack()

        L6 = Label(MainFrame, text=" Meals(yes/no)")
        L6.pack()
        Input6 = Entry(MainFrame)
        Input6.pack()

        L7 = Label(MainFrame, text="Number of People per Room")
        L7.pack()
        Input7 = Entry(MainFrame)
        Input7.pack()

        BottomFrame = Frame(BookingGUI)
        BottomFrame.pack()
        Btn = Button(BottomFrame, text="Confirm Registration", command=Store)
        Btn.pack()
        BookingGUI.mainloop()

    def DateDif(self):
        return (self.check_out - self.check_in).days

    def Logs(self):
        fileA = open("Logs.txt", "a")
        LogMember = (str(self.RegisterObj.memberID)
                     + "," + str(self.RegisterObj.password)
                     + "," + str(self.RegisterObj.age)
                     + "," + str(self.RegisterObj.email)
                     + "," + str(self.roomID)
                     + "," + str(self.city)
                     + "," + str(self.check_in)
                     + "," + str(self.check_out)
                     + "," + str(self.breakfast)
                     + "," + str(self.NofA)
                     + "\n")
        fileA.writelines(LogMember)

