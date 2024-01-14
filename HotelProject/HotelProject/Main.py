import datetime
import os
import roomBooking
import Prices
import Forms
from tkinter import *

class Main(Prices.priceCheck):
    def __init__(self):
        super().__init__()

def Room_Options():
    hotelFile = open("Hotel_Info.txt", "r")
    alldata = hotelFile.readlines()

    roomWindow = Toplevel()
    roomWindow.title("Available Rooms")

    Output = Text(roomWindow, height=20, width=40, bg="black", fg="white")
    Output.pack(pady=10)

    for x in alldata:
        data = x.strip().split(",")
        printing = "Room: " + data[0] + " City: " + data[1] + " Price: " + data[2] + "\n"
        Output.config(state=NORMAL)
        Output.insert(END, printing)
    Output.config(state=DISABLED)

M = Main()
Menu = Tk()
Menu.configure(bg="black")

TopFrame = Frame(Menu, bg="#808080")
TopFrame.pack(side=TOP, pady=30)

Welcome_Label = Label(TopFrame, text="Mohannad , Hashim Managment System ", font=('Arial', 40, 'italic'), fg="#FFFFFF", bg="#808080")
Welcome_Label.pack(side=LEFT, padx=20)

LogoImage = PhotoImage(file="Hotel.png").subsample(1, 1)
Logo = Label(TopFrame, text="Test", image=LogoImage, fg="#FFFFFF", bg="#808080")
Logo.pack(side=RIGHT, padx=50)

F1 = Frame(Menu, bg="black")
F1.pack(pady=20)  

button_font = ('Arial', 14)
RegisterM_Button = Button(F1, text="Register Member", command=M.RegisterObj.InputMember, height=5, width=100, font=button_font)
RegisterM_Button.pack(pady=10)

Booking_Button = Button(F1, text="Book", command=M.InputBooking, height=5, width=100, font=button_font)
Booking_Button.pack(pady=10)

GetReceipt = Button(F1, text="Receipt", command=M.Receipt, height=5, width=100, font=button_font)
GetReceipt.pack(pady=10)

Review = Button(F1, text="Review", command=Forms.SubmitReview, height=5, width=100, font=button_font)
Review.pack(pady=10)

SeeRooms = Button(F1, text="See Rooms", command=Room_Options, height=5, width=100, font=button_font)
SeeRooms.pack(pady=10)

F2 = Frame(Menu, bg="black")
F2.pack(side=RIGHT)

Menu.mainloop()
