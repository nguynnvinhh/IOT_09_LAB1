
import paho.mqtt.client as mqtt
import json

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "iot/lab/sensor01/data"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi MQTT broker")
        client.subscribe(TOPIC)
    else:
        print("Ket noi that bai:", reason_code)


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        print("\nDevice:", data["device_id"])
        print("Temperature:", data["temperature"], "C")
        print("Humidity:", data["humidity"], "%")

        if data["temperature"] > 35:
            print("CANH BAO: Nhiet do cao")

        if data["humidity"] < 40:
            print("CANH BAO: Do am thap")

    except (ValueError, KeyError, TypeError) as e:
        print("Du lieu khong hop le:", e)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()
    print("Da dung monitoring")
