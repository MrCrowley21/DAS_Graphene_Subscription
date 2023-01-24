import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import logging
from email.utils import formataddr

logging.basicConfig(level=logging.DEBUG)


# class to manipulate emails
class EmailManipulator:
    @staticmethod
    def send_email(receiver_email, otp):
        try:
            # Create your SMTP session
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            # Use TLS to add security
            smtp.starttls()
            # User Authentication
            smtp.login("sender_mail", "app_password")
            sender = "sender_mail"
            receiver = receiver_email
            msg = MIMEMultipart('alternative')
            # Defining The Subject
            msg['Subject'] = "We are glad to welcome you!"
            msg['From'] = formataddr(('Lost&Found Team', 'sender_mail'))
            # Defining The Message
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # date
            # Defining email text
            html = """\
            <html>
              <head></head>
              <body>
                <p><b>Your OTP for authentication</b><br>
                   <b>Date</b>: %s<br>
                   <b>OTP</b>: %s<br>
                   With respect,<br>
                   Lost&Found Team
                </p>
              </body>
            </html>
            """ % (date, otp)
            text = MIMEText(html, 'html')
            msg.attach(text)
            # Sending the Email
            smtp.sendmail(sender, receiver, msg.as_string())
            #  Terminating the session
            smtp.quit()
            logging.info(f"Email sent successfully!")
        except Exception as ex:
            logging.info(f"Something went wrong....", ex)
