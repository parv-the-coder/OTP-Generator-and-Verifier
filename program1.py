# GUI- Graphical User Interface
from tkinter import *

from program2 import *

# to call other program in terminal
from subprocess import call

# Tk is passed to use its methods like
class Generate_otp(Tk):

    def __init__(self):

        super().__init__()

    # To Create window
        self.geometry("1000x580+200+80")

    # Configure is used for formatting-To set Background Colour
        self.configure(bg="#FFFFFF")

    # Restrict to resize window
        self.resizable(False, False)

    # Font Style & Size
        self.f = ("Times bold", 14)

    def Labels(self):

    # For setting Blue Colour in window
        self.upper_frame = Frame(self, bg="#4682B4", width=1500, height=130)

    # From where to where
        self.upper_frame.place(x=0, y=0)

    # For setting Blue Colour in window
        self.lower_frame = Frame(self, bg="#4682B4", width=1500, height=200)

    # From where to where
        self.lower_frame.place(x=0, y=270)

    # To Display Image in label & buttons and it does not require any external image viewer or web browser
        self.picture = PhotoImage(file="password1.png")

    # Label is used to specify the container box where we can place the text or images
        self.k = Label(self.upper_frame, image=self.picture,
                       bg="#4682B4").place(x=220, y=35)

    # FG to set text color
        self.j = Label(self.upper_frame, text="OTP Verification",
                       font="TimesNewRoman 38 bold", bg="#4682B4", fg="white").place(x=330, y=35)

        self.a = Label(self, text="OTP is valid for 10 minutes.",
                       font="TimesNewRoman 14", bg="#4682B4", fg="white").place(x=360, y=290)

        self.b = Label(self, text="Click on the Generate OTP button to generate OTP.",
                       font="TimesNewRoman 14", bg='#4682B4', fg="white").place(x=260, y=338)

        self.logo = PhotoImage(file="Logo1.png")

        self.d = Label(self, image=self.logo, fg="white").place(x=885, y=475)

    def Buttons(self):

        self.GenerateOTP = PhotoImage(file="Generate_OTP.png")

    # Button to create a clickable button
    # Command sets the function to be called when the button is clicked
    # Border=0 to remove the border around button
        self.generatebutton = Button(
            self, image=self.GenerateOTP, command=self.Open, border=0)
        self.generatebutton.place(x=390, y=390)

    def Open(self):

        # Close a GUI window
        program1 = self.destroy()

    # First parameter  is for interpreter
    # Second parameter is for program which will be executed
        call(["python", "program2.py"])


# function will only be called if the script is run directly (i.e., not imported as a module)
if __name__ == "__main__":

    window = Generate_otp()
    window.Labels()
    window.Buttons()

# mainloop() method starts the event loop and keeps the window open until the user closes it.
    window.mainloop()
