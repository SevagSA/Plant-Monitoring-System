# Python program to illustrate how we would run the instances together
# The button code would always be running, while the temp and humidity will execute once an hour
import threading
import time


def get_temperature():
    while True:
        print("Getting the temperature")
        # our temperature code here
        time.sleep(10) # in our code, it will be an hour


def get_humidity():
    while True:
        print("Getting the humidity")
        # our temperature code here
        time.sleep(10) # in our code, it will be an hour


def button_toggle():
    # add our actual button code here
    while True:
        print("OFF")
        print("ON")
        time.sleep(1) 


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=get_temperature)
    t2 = threading.Thread(target=get_humidity)
    t3 = threading.Thread(target=button_toggle)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    t3.start()
