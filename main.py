# main.py
from otpverifier import OTPVerifier
from interface import OTPInterface

if __name__ == "__main__":
    otp_verifier = OTPVerifier()
    otp_interface = OTPInterface(otp_verifier)
    otp_interface.run()
