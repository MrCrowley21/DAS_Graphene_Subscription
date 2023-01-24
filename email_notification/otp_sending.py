import pyotp
import time

from email_sending import *

email_manipulator = EmailManipulator()


def send_otp_code(email, hotp_at):
    secret_code = pyotp.random_base32()
    hotp = pyotp.HOTP(secret_code)
    code = hotp.at(hotp_at)
    email_manipulator.send_email(email, code)
    return code


if __name__ == "__main__":
    send_otp_code('', int(time.time()))
