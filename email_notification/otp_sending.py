import pyotp
import time

from email_sending import *

email_manipulator = EmailManipulator()


def send_otp_code(email, hotp_at):
    secret_code = pyotp.random_base32()
    hotp = pyotp.HOTP(secret_code)
    code = hotp.at(hotp_at)
    email_manipulator.send_email(email, code)
    return secret_code, hotp_at


def check_otp_code(secret_code, hotp_at, otp_data):
    if pyotp.HOTP(secret_code).verify(otp_data, hotp_at):
        return True
    else:
        return False


if __name__ == "__main__":
    secret_code, hotp_at = send_otp_code('receiver_email', int(time.time()))
    user_otp = input()
    print(check_otp_code(secret_code, hotp_at, user_otp))
