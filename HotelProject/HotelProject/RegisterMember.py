from tkinter import *

class Register:

    def __init__(self, memberID=1001, password="password", age=0, email="@gmail.com"):
        self.memberID = memberID
        self.password = password
        self.age = age
        self.email = email

    def InputMember(self):
        def Store():
            MemberCheck = open("MemberRoom.txt", "r")
            alldata = MemberCheck.readlines()
            for x in alldata:
                d = x.strip().split(",")
                if Input1.get() != d[0]:
                    self.memberID= Input1.get()
                    self.password = Input2.get()
                    self.age = Input3.get()
                    self.email = Input4.get()
                    SuccessLbl = Label(BottomFrame, text="Successfully Registered")
                    SuccessLbl.pack()
                    break
                else:
                    ErrorLbl = Label(BottomFrame, text="Member Already Used")
                    ErrorLbl.pack()
                    break


        RegisterGUI = Tk()
        RegisterGUI.configure(bg="black",height=4,width=30)

        MainFrame = Frame(RegisterGUI)
        MainFrame.pack()

        FrameVariables = Frame(RegisterGUI)
        FrameVariables.pack()

        L1 = Label(FrameVariables, text="Enter ID",height=4,width=30)
        L1.pack()
        Input1 = Entry(FrameVariables)
        Input1.pack()

        L2 = Label(FrameVariables, text="Enter Password",height=4,width=30)
        L2.pack()
        Input2 = Entry(FrameVariables)
        Input2.pack()

        L3 = Label(FrameVariables, text="Enter Age",height=4,width=30)
        L3.pack()
        Input3 = Entry(FrameVariables)
        Input3.pack()

        L4 = Label(FrameVariables, text="Enter Email",height=4,width=30)
        L4.pack()
        Input4 = Entry(FrameVariables)
        Input4.pack()

        BottomFrame = Frame(RegisterGUI)
        BottomFrame.pack(pady=10)
        Btn = Button(BottomFrame, text="Confirm Registration", command=Store,height=4,width=30)
        Btn.pack()
        RegisterGUI.mainloop()

