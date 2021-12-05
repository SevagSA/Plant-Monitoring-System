from .dc_motor import motor_on
# from .DHT import get_temp, get_humid
from .sending_receiving_email import execute_email_service
from .sending_email import email_send
from .bt_rssi import get_device_information


def get_temperature():
    return 12
    # return get_temp()


def send_email():
    pass
    # return execute_email_service()


def get_humidity():
    pass
    # return get_humid()


def dc_motor_on():
    pass
    # motor_on()


def led_on():
    pass
    # email_send()


def get_light():
    return 600


def get_information(threshold):
    pass
    # return get_device_information(threshold)
