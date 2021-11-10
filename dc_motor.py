import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 23
Motor1B = 24
Motor1E = 25
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
def motor_on():
    print ("Turning motor on")
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    pwm = GPIO.PWM(Motor1E,100)
    pwm.start(0)
    pwm.ChangeDutyCycle(100)


def motor_off():
    print ("Stopping motor")
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.cleanup()


