# python3.6

import random

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "#"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message
    
    ##PSEUDO CODE:
    #user_ids = [1231412, 123455621]
    #current_user_id = null
    #photoresistor_value = null
    
    #if (topic is equal to "room/RFID"):
        #for {id} in {user_ids}:
            #if (message is equal to {id}):
                #current_user_id = {id} #Then, retrieve the user with a matching id and use his information to perform the rest of the processing.
                
    #if (topic is equal to "room/Photoresistor"):
        #save into a variable the MQTT message (The MQTT message would contain the photoresistor value)
        #photoresistor_value = the MQTT message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
