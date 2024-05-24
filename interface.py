# interface.py
from tkinter import Tk, Label, Entry, Button

class OTPInterface:
    def __init__(self, otp_verifier):
        self.otp_verifier = otp_verifier

        self.root = Tk()
        self.root.geometry("400x200")
        self.root.title("OTP Interface")

        self.label = Label(self.root, text="Enter OTP:")
        self.label.pack(pady=10)

        self.otp_entry = Entry(self.root)
        self.otp_entry.pack(pady=10)

        self.submit_button = Button(self.root, text="Submit", command=self.verify_otp)
        self.submit_button.pack(pady=10)

    def verify_otp(self):
        entered_otp = self.otp_entry.get()
        if self.otp_verifier:
            self.otp_verifier.check_otp(entered_otp)
        else:
            print("Error: OTPVerifier instance is not provided.")
        self.root.destroy()

    def run(self):
        self.root.mainloop()

