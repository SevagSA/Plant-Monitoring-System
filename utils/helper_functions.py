# import time
# import board
# import adafruit_dht
# from .DHT import get_temp, get_humid
from .dc_motor import motor_on

import random

# dht_device = adafruit_dht.DHT11(board.D22)

def get_temperature():

   return get_temp()

def get_humidity():
   return get_humid()

def dc_motor_on():
    motor_on()
