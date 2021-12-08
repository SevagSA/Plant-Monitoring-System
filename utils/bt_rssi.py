import os
import re


def get_device_information():
    """
    Get all bluetooth devices in proximity of the RPi.
    """
    devices = os.system('sudo /usr/bin/node bluetoothTest.js > output.txt')
    device_list = []
    rss_list = []
    information_dict = {}
    with open('output.txt', encoding='utf-8-sig', errors='ignore') as devices:
        sp = devices.read().splitlines()

    for line in sp:
        rssi = 0
        transmitterId = ""
        if "transmitterId:" in line:
            transmitterId = line.split("'")[1::2]
            device_list.append(transmitterId)
        if "rssi:" in line:
            rssi = int(re.search(r'\d+', line).group(0))
            rss_list.append(rssi)
    for i in range(len(device_list)):
        information_dict[device_list[i][0]] = rss_list[i]
    return information_dict
