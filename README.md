# OTP Generator and Verifier

This repository contains two programs: a GUI-based OTP (One-Time Password) Generator and a Verification system implemented in Python. The OTP Generator generates a random 4-digit OTP and sends it to a specified phone number using the Twilio API. The Verification system allows users to enter the OTP received and verifies its correctness.

# Program 1: GUI OTP Generator

The GUI OTP Generator program utilizes the Tkinter library to create a graphical user interface. It allows users to generate an OTP and initiate the OTP verification process. The generated OTP is valid for 10 minutes. Upon generating the OTP, users can proceed to the OTP verification by clicking the "Generate OTP" button.

# Program 2: OTP Verifier

The OTP Verifier program verifies the OTP entered by the user. It relies on the Twilio API to send the OTP to the user's phone number. The program prompts the user to enter the OTP received and checks its validity. If the OTP is correct, a success message is displayed. Otherwise, an error message is shown.

# Dependencies

The OTP Generator and Verifier programs rely on the following dependencies:

   1) Twilio: Used to send SMS messages for OTP delivery.
   2) Tkinter: Used to create the graphical user interface.

Make sure you have these dependencies installed before running the programs.

# Configuration

To use the Twilio API for OTP delivery, you need to provide your own Twilio Account SID and Auth Token. Update the respective placeholders in the code with your Twilio credentials.

self.client = Client("Your SID", "SID KEY")

Replace "Your SID" with your Twilio Account SID and "SID KEY" with your Twilio Auth Token.

# Note

Please note that the phone number receiving the OTP needs to be registered with Twilio for the OTP delivery to work. Ensure that you have a valid Twilio account and phone number configured.

# Contributing

If you'd like to contribute to the OTP Generator and Verifier project, feel free to create a pull request or open an issue. Your contributions are highly appreciated.
