from .dc_motor import motor_on
from .DHT import get_temp, get_humid
from .sending_receiving_email import execute_email_service
from .sending_email import email_send
from .bt_rssi import get_number_devices, get_device_information


def get_temperature():
    # return get_temp()
    return 1

def send_email():
    return execute_email_service()

def get_humidity():
    #  return get_humid()
    return 1

def dc_motor_on():
    # motor_on()
    return 1

def led_on():
    email_send()
    
def get_light():
   return 600

def get_information(threshold):
    return get_device_information(threshold)
