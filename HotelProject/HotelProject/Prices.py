import datetime
import RegisterMember
import roomBooking
from tkinter import *


class priceCheck(roomBooking.Booking):
    def __init__(self):
        super().__init__()

    def GetTotalPrice(self):
        price = 0
        File = open("Hotel_Info.txt", "r")
        allData = File.readlines()
        for x in allData:
            d = x.strip().split(",")
            if d[0] == str(self.roomID):
                price = int(d[2])
        total = price * int(self.DateDif())

        tax = 0
        if self.city == "Rome":
            tax += 100
        elif self.city == "Bolzano ":
            tax += 50
        elif self.city == "Milan ":
            tax += 10
        if self.business:
            return total - (total * 0.25) + tax
        return total + tax

    def Receipt(self):
        main = Tk()
        TopF = Frame(main)
        TopF.pack(side=TOP)
        VarName = Frame(TopF)
        VarValue = Frame(TopF)
        VarName.pack(side=LEFT)
        VarValue.pack(side=RIGHT)

        LN1 = Label(VarName, text="ID:")
        LV1 = Label(VarValue, text=str(self.RegisterObj.memberID))

        LN2 = Label(VarName, text="Room ID:")
        LV2 = Label(VarValue, text=str(self.roomID))

        LN3 = Label(VarName, text="City:")
        LV3 = Label(VarValue, text=str(self.city))

        LN4 = Label(VarName, text="Check-In:")
        LV4 = Label(VarValue, text=str(self.check_in))

        LN5 = Label(VarName, text="Check-Out:")
        LV5 = Label(VarValue, text=str(self.check_out))

        LN6 = Label(VarName, text="Total Days:")
        LV6 = Label(VarValue, text=str(self.DateDif()))

        LN7 = Label(VarName, text="Total Amount:")
        LV7 = Label(VarValue, text=str(self.GetTotalPrice()) + "$")

        LN8 = Label(VarName, text="Date Reserved:")
        LV8 = Label(VarValue, text=str(datetime.date.today()))

        LN9 = Label(VarName, text="Gets Discount?:")
        LV9 = Label(VarValue, text=str(self.business))

        LN10 = Label(VarName, text="Meals?")
        LV10 = Label(VarValue, text=str(self.breakfast))

        LN11 = Label(VarName, text="Number of People:")
        LV11 = Label(VarValue, text=str(self.NofA))

        LN1.pack()
        LV1.pack()
        LN2.pack()
        LV2.pack()
        LN3.pack()
        LV3.pack()
        LN4.pack()
        LV4.pack()
        LN5.pack()
        LV5.pack()
        LN6.pack()
        LV6.pack()
        LN7.pack()
        LV7.pack()
        LN8.pack()
        LV8.pack()
        LN9.pack()
        LV9.pack()
        LN10.pack()
        LV10.pack()
        LN11.pack()
        LV11.pack()
        main.mainloop()
