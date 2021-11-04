# import time
# import board
# import adafruit_dht
# from DHT import get_temp_and_humidity

# dht_device = adafruit_dht.DHT11(board.D22)

def get_temperature() -> int:
    """
    This is going to return 1 temp at the given time.
    Maybe: Have a dict of all temps in the intial_dashboard.py file
    and with the key being the time of day that the function 
    called this function, i.e. get_temperature() and the value
    would be the temperature, i.e the return value of this function
    """
    # temperature_received = get_temp_and_humidity()[0]
    # print("This is the temperature :" , temperature_received)
    # return temperature_received
    return 1

def get_humidity() -> int :
    # humidity_received = get_temp_and_humidity()[1]
    # print("This is the temperature :" , humidity_received)
    # return humidity_received
    return 2