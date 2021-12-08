import smtplib
# import RPi.GPIO as GPIO
import ssl
import time
# GPIO.setwarnings(False)
led = 33


def email_send():
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(led,GPIO.OUT)
    # GPIO.output(led,1)
    # time.sleep(10)
    # GPIO.output(led,0)
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
    print("sending")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("sent email!")

def user_send_email(message):
    # GPIO.setmode(GPIO.BOARD)
    # GPIO.setup(led,GPIO.OUT)
    # GPIO.output(led,1)
    # time.sleep(10)
    # GPIO.output(led,0)
    sender = "vanieraliiot@gmail.com"
    password = "CrazyChicken123"
    receiver = "vanieraliiot@gmail.com"
    port = 465
    subject = "Welcome message"
    message = 'Subject: {}\n\n{}'.format(subject, message)
    context = ssl.create_default_context()
    print("sending")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("sent email!")
