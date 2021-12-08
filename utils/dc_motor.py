import RPi.GPIO as GPIO
from time import sleep


def motor_on():
    """
    Turn the DC motor on for 4 seconds using PWM.
    """

    GPIO.setmode(GPIO.BOARD)

    Motor1A = 16
    Motor1B = 18
    Motor1E = 22

    GPIO.setwarnings(False)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    pwm = GPIO.PWM(Motor1E, 100)
    pwm.start(0)
    pwm.ChangeDutyCycle(100)
    sleep(4)
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.cleanup()
