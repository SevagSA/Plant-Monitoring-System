import smtplib
import RPi.GPIO as GPIO
import time
import ssl
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
led = 26
button = 6
def email():
    sender ="vanieraliiot@gmail.com"
    password = "password"
    receiver = "vanieraliiot@gmail.com"
    port = 465
    subject = "Temperature Threshhold Reached"
    text = """
        Would you like to turn on the fan? YES or NO.
        -Your Team.
        """
    message = 'Subject: {}\n\n{}'.format(subject, text)
    context = ssl.create_default_context()
    print("sending")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("sent email!")
GPIO.setup(led,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
switchedOn = False
while True:
     button_state = GPIO.input(button)
     if button_state == False:
         if switchedOn == False:
             switchedOn = True
             GPIO.output(led,1)
             email()
             GPIO.output(led,0)
             switchedOn = False
             GPIO.output(led,0)

            
            
    
        
        
            
        
    
        
         

    
