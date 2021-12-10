from .dc_motor import motor_on
from .DHT import get_temp, get_humid
from .sending_receiving_email import execute_email_service
from .sending_email import email_send, user_send_email
from .bt_rssi import get_device_information


def get_temperature():
    """
    Get the current temperatue of the enviroment.
    """
    return get_temp()


def send_email():
    """
    Send an email to ask the adminitrator to turn the fan on.
    """
    execute_email_service()


def user_login(message):
    """
    Send an email welcoming the user loggin in.
    """
    return user_send_email(message)


def get_humidity():
    """
    Get the current humidity of the enviroment.
    """
    return get_humid()


def dc_motor_on():
    motor_on()


def led_on():
    """
    Send an email notifying that the light threshold has been reached.
    """
    email_send()


def get_information():
    """
    Get all relevant data of all bluetooth devices in proximity.
    """
    return get_device_information()
