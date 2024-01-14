from tkinter import *
def SubmitReview():
    def SendReview():
        File = open("FormLog.txt", "a")
        strAdd = str(Review_Entry.get()) + "|" + str(Rating_Entry.get() + "/5")
        File.writelines(strAdd + "\n")
        File.close()

    ReviewWindow = Tk()
    SingleFrame = Frame(ReviewWindow)
    SingleFrame.pack()

    Review_Label = Label(SingleFrame, text="Enter Feedback About your stay")
    Review_Label.pack()
    Review_Entry = Entry(SingleFrame)
    Review_Entry.pack()

    Rating_Label = Label(SingleFrame, text="Enter Rating out of 5", height= 5 , width=20)
    Rating_Label.pack()
    Rating_Entry = Entry(SingleFrame)
    Rating_Entry.pack()

    Send_Button = Button(SingleFrame, text="Submit", command=SendReview,width=20,height=2)
    Send_Button.pack()

    ReviewWindow.mainloop()

