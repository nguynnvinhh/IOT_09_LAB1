
import paho.mqtt.client as mqtt
from datetime import datetime

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "iot/lab/message"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi MQTT broker")
        client.subscribe(TOPIC)
    else:
        print("Ket noi that bai:", reason_code)


def on_message(client, userdata, msg):
    print("\nNhan duoc message:")
    print("Topic:", msg.topic)
    print("Payload:", msg.payload.decode())
    print("Time:", datetime.now().strftime("%H:%M:%S"))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()
    print("Da dung subscriber")
