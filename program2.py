# For SID & Token
from twilio.rest import Client

# To generate random number for OTP
import random

import time

from tkinter import *
from tkinter import messagebox


class otp_verifier(Tk):
    def __init__(self):
        super().__init__()

    # To Create window
        self.geometry("1000x580+200+80")

    # Configure is used for formatting-To set Background Colour
        self.configure(bg="#FFFFFF")

    # Restrict to resize window
        self.resizable(False, False)

        self.n = str(self.OTP())

    # The Account SID, which acts as a username, and the Auth Token which acts as a password
        self.client = Client("Your SID",
                             "SID KEY")

    # To send SMS Message
        self.client.messages.create(
            to=("your phone number"), from_="+14752675284", body=self.n)

    # StringVar is a class used to create a mutable string variable
        self.minuteString = StringVar()
        self.secondString = StringVar()

    # Set strings to default value
        self.minuteString.set("10")
        self.secondString.set("00")

    def Labels(self):

        # The Canvas is a rectangular area intended for drawing pictures or other complex layouts.
        self.c = Canvas(self, bg="#808080", width=400, height=280)

    # To place canvas
        self.c.place(x=290, y=120)

    # Entry widget is used to provde the single line text-box
        self.minuteTextbox = Entry(self, width=2, bg="#808080", font=(
            "Calibri", 20, ""), textvariable=self.minuteString)

        self.secondTextbox = Entry(self, width=2, bg="#808080", font=(
            "Calibri", 20, ""), textvariable=self.secondString)

    # Center textboxes
        self.minuteTextbox.place(x=460, y=270)
        self.secondTextbox.place(x=500, y=270)

    # For setting  Colour in window
        self.upper_frame = Frame(self, bg="#4682B4", width=1500, height=130)
        self.upper_frame.place(x=0, y=0)

    # To Display Image in label & buttons and it does not require any external image viewer or web browser
        self.picture = PhotoImage(file="password1.png")

    # Label is used to specify the container box where we can place the text or images
        self.k = Label(self.upper_frame, image=self.picture,
                       bg="#4682B4").place(x=190, y=35)

    # FG to set text color
        self.j = Label(self.upper_frame, text="Verify OTP",
                       font="TimesNewRoman 38 bold", bg="#4682B4", fg="white").place(x=290, y=35)

        self.s_logo = PhotoImage(file="Logo2.png")

        self.d = Label(self, image=self.s_logo,
                       fg="#FFFFFF").place(x=845, y=440)

    def Entry(self):

        # Text widget is used to display the multi-line formatted text with various styles and attributes
        self.User_Name = Text(self, font="calibri 20",
                              borderwidth=5, wrap=WORD, width=23, height=1)
        self.User_Name.place(x=330, y=200)

    def OTP(self):

        # To Generate 4 digit random OTP
        return random.randrange(1000, 10000)

    def Buttons(self):

        self.submitButtonImage = PhotoImage(file="sub.png")

    # Button to create a clickable button

        self.submitButton = Button(self, image=self.submitButtonImage, command=lambda: [
                                   self.checkOTP(), self.runTimer()], border=0)
        self.submitButton.place(x=440, y=330)

        self.resendOTPImage = PhotoImage(file="resendotp.png")
        self.resendOTP = Button(
            self, image=self.resendOTPImage, command=self.resendOTP(),  border=0)
        self.resendOTP.place(x=420, y=430)

    def resendOTP(self):

        self.n = str(self.OTP())
        self.client = Client("ACc27dc84957bc5ab4eb0e5eb9953760d7",
                             "7cd977b32573ef2d6473c14f603cab30")
        self.client.messages.create(
            to=("+919099142477"), from_="+14752675284", body=self.n)

    def checkOTP(self):
        try:

            # The get() method of the text widget is being used here, which takes two arguments: the starting and ending index of the text to be retrieved. In this case, the starting index is 1.0, which means the beginning of the second line of text, and the ending index is "end-1c", which means the end of the text minus the final newline character. This ensures that any trailing newline character is removed from the input.
            self.userInput = int(self.User_Name.get(1.0, "end-1c"))

            if self.userInput == int(self.n):

                # messagebox is a module in Python's standard library that provides a way to create message boxes or dialogs.
                # showinfo() is a function within the messagebox module that displays a message box with an OK button and an icon representing an informational message
                messagebox.showinfo("Showinfo", "Verification Successful")
                self.n = "done"
            else:
                messagebox.showinfo("Showinfo", "Wrong OTP")
        except:
            messagebox.showinfo("Showinfo", "Invalid OTP ")

    def runTimer(self):

        self.clockTime = int(self.minuteString.get()) * \
            60 + int(self.secondString.get())

        while (self.clockTime > -1):

            # divmod() is a built-in Python function that returns the quotient and remainder when one integer is divided by another
            totalMinutes, totalSeconds = divmod(self.clockTime, 60)

            self.minuteString.set("{0:2d}".format(totalMinutes))
            self.secondString.set("{0:2d}".format(totalSeconds))

        # Update the interface
            self.update()
            time.sleep(1)

        # Let the user know if the timer has expired
            if (self.clockTime == 0):
                messagebox.showinfo("", "Your time has expired!")

            self.clockTime -= 1


# function will only be called if the script is run directly (i.e., not imported as a module)
if __name__ == "__main__":
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.OTP()
    window.Buttons()
    window.update()

# mainloop() method starts the event loop and keeps the window open until the user closes it.
    window.mainloop()
