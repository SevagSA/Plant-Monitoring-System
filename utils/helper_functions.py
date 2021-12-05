from .dc_motor import motor_on
from .DHT import get_temp, get_humid
from .sending_receiving_email import execute_email_service
from .sending_email import email_send, user_send_email
from .bt_rssi import get_device_information


def get_temperature():
    return get_temp()


def send_email():
    return execute_email_service()


def user_login(message):
    return user_send_email(message)

def get_humidity():
    return get_humid()


def dc_motor_on():
    motor_on()


def led_on():
    email_send()


def get_information():
    return get_device_information()
