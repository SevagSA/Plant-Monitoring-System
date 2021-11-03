# import time
# import board
# import adafruit_dht

dht_device = adafruit_dht.DHT11(board.D22)

def get_temperature() -> int:
    """
    This is going to return 1 temp at the given time.
    Maybe: Have a dict of all temps in the intial_dashboard.py file
    and with the key being the time of day that the function 
    called this function, i.e. get_temperature() and the value
    would be the temperature, i.e the return value of this function
    """
    # temperature_received = dht_device.temperature
    # print("This is the temperature :" , temperature_received)
    # return temperature_received
    # return [20, 21, 23, 19, 18]
    return 2

def get_humidity() -> int :
    # humidity_received = dht_device.humidity
    # print("This is the temperature :" , humidity_received)
    # return humidity_received
    # return [60, 75, 55, 67, 90]
    return 1