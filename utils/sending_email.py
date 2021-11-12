import smtplib
import RPi.GPIO as GPIO
import ssl
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
led = 26
def email():
    sender ="vanieraliiot@gmail.com"
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
GPIO.setup(led,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
email()
GPIO.output(led,1)


            
            
    
        
        
            
        
    
        
         

    
