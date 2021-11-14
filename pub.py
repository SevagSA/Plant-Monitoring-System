# import dash_mqtt
# import dash
# from dash import dcc, html
# from dash.dependencies import Input, Output, State

# TEST_SERVER = 'test.mosquitto.org'
# TEST_SERVER_PORT = 8083
# TEST_SERVER_PATH = 'mqtt'
# MESSAGE_OUT_TOPIC = 'testtopic'
# MESSAGE_IN_TOPIC = 'testtopic'

# app = dash.Dash(__name__)

# app.layout = html.Div([
#     dash_mqtt.DashMqtt(
#         id='mqtt',
#         broker_url=TEST_SERVER,
#         broker_port=TEST_SERVER_PORT,
#         broker_path=TEST_SERVER_PATH,
#         topics=[MESSAGE_IN_TOPIC]
#     ),
#     html.H1('MQTT echo'),
#     html.P('MQTT echo server to ' + TEST_SERVER +
#            ' on port ' + str(TEST_SERVER_PORT)),
#     dcc.Input(
#         id='message_to_send',
#         placeholder='message to send',
#         debounce=True),
#     html.Button('Send', id='send'),
#     html.Div(id='return_message')
# ])


# @app.callback(
#     Output('mqtt', 'message'),
#     Input('send', 'n_clicks'),
#     State('message_to_send', 'value')
# )
# def display_output(n_clicks, message_payload):
#     if n_clicks and n_clicks > 0:
#         print("message_playload: ", message_payload)
#         return {
#             'topic': MESSAGE_OUT_TOPIC,
#             'payload': message_payload
#         }
#     return dash.no_update


# @app.callback(
#     Output('return_message', 'children'),
#     Input('mqtt', 'incoming')
# )
# def display_incoming_message(incoming_message):
#     if (incoming_message):
#         return incoming_message['payload']
#     else:
#         return dash.no_update


# if __name__ == '__main__':
#     app.run_server(debug=True, port=8081)

# python 3.6

import random
import time

from paho.mqtt import client as mqtt_client


broker = 'broker.emqx.io'
port = 1883
topic = "room/light"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'


def connect_mqtt():
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


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"{msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
