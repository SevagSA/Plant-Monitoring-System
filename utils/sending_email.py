import smtplib
import ssl
import time



def email_send():
    """
    Sends an email to the user that the light levels have exceeded given threshold
    """
    sender = "vanieraliiot@gmail.com"
    password = "CrazyChicken123"
    receiver = "vanieraliiot@gmail.com"
    port = 465
    subject = "Light Threshhold Reached"
    text = """
        The Light threshhold has been reached and the LED's have been turned on.
        """
    message = 'Subject: {}\n\n{}'.format(subject, text)
    context = ssl.create_default_context()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)


def user_send_email(message):
    """
    Sends an email to the user with any message provided
    """
    sender = "vanieraliiot@gmail.com"
    password = "CrazyChicken123"
    receiver = "vanieraliiot@gmail.com"
    port = 465
    subject = "Welcome message"
    message = 'Subject: {}\n\n{}'.format(subject, message)
    context = ssl.create_default_context()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
