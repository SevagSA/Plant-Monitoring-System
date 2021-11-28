import bluetooth
import bluetooth._bluetooth as bt
import struct
import array
import fcntl
import os
import json
import re

def get_device_information():
    devices = os.system('sudo /usr/bin/node ../bluetoothTest.js > output.txt')
    deviceList = []
    rssiList = []
    informationDict = {}
    with open('output.txt',encoding='utf-8-sig', errors='ignore') as devices:
         sp = devices.read().splitlines()
        
    for line in sp:
        rssi = 0;
        transmitterId = "";
        if "transmitterId:" in line:
            transmitterId = line.split("'")[1::2]
            deviceList.append(transmitterId)
        if "rssi:" in line:
            rssi = int(re.search(r'\d+', line).group(0))
            rssiList.append(rssi)
    for i in range(len(deviceList)):
        informationDict[deviceList[i][0]] = rssiList[i]
    return(informationDict)