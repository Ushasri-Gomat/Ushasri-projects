# otp_verifier.py
from twilio.rest import Client
import random
from tkinter import messagebox

class OTPVerifier:
    def __init__(self):
        self.n = str(self.generate_otp())
        self.client = Client("AC55bb39e4ca091465fea88f140f150960", "198a46143d0b42e3e8450ada308de5a3")
        self.client.messages.create(to=("+919951270104"),
                                    from_="+15086894246",
                                    body=self.n)

    def generate_otp(self):
        return random.randrange(1000, 10000)

    def check_otp(self, entered_otp):
        try:
            user_input = int(entered_otp)
            if user_input == int(self.n):
                messagebox.showinfo("showinfo", "Verification Successful")
                self.n = "done"
            else:
                messagebox.showinfo("showinfo", "Wrong OTP")
        except ValueError:
            messagebox.showinfo("showinfo", "Invalid OTP ")


