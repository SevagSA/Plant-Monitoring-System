import smtplib
import RPi.GPIO as GPIO
import time
import ssl
import email
import imaplib
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

def sendEmail(text):
    sender ="vanieraliiot@gmail.com"
    password = "password"
    receiver = "vanieriotali2@gmail.com"
    port = 465
    subject = "From Rpi Ali Lezzeik"
    message = 'Subject: {}\n\n{}'.format(subject, text)
    context = ssl.create_default_context()
    print("sending")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("sent email!")

def receiveEmailChecker() :
    while True:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('vanieraliiot@gmail.com', 'password')
        mail.list()
        mail.select("inbox") # connect to inbox.
        result, data = mail.search(None, "(UNSEEN)")

        ids = data[0]
        id_list = ids.split() 
        if(len(id_list)) > 0:
            latest_email_id = id_list[-1] 
        else:
            return "Nothing"
        result, data = mail.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1] 
        decoded_data = email.message_from_string(raw_email.decode("utf-8"))
        if type(decoded_data.get_payload()[0]) is str:
            break
        else:
            text = decoded_data.get_payload()[0].get_payload();
            answer1 = text[0:3].lower()
            answer2 = text[0:2].lower()
            if(answer1 == "yes"):
                return "yes"
            elif(answer1 == "no"):
                return "no"
            else:
                return "Invalid"
=
question = input("Would you like to turn on the fan? yes or no : ")
sendEmail(question)
while True:
    answer = receiveEmailChecker()
    if( answer == 'yes'):
         print("On")
         break
    elif(answer == 'no'):
        print("Off")
        break
    else :
        print("Checking inbox for emails...")
        time.sleep(3)
        
    
        




