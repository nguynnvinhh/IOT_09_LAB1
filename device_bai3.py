
import paho.mqtt.client as mqtt
import json

BROKER = "broker.emqx.io"
PORT = 1883

CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

status = "OFF"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Den light01 da ket noi MQTT")
        client.subscribe(CMD_TOPIC)
    else:
        print("Ket noi that bai:", reason_code)


def on_message(client, userdata, msg):
    global status

    command = msg.payload.decode().strip().upper()

    if command not in ("ON", "OFF"):
        print("Lenh khong hop le:", command)
        return

    status = command

    data = {
        "device_id": "light01",
        "status": status
    }

    client.publish(STATUS_TOPIC, json.dumps(data), qos=1)

    print("Nhan lenh:", command)
    print("Trang thai den:", status)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

try:
    client.loop_forever()
except KeyboardInterrupt:
    client.disconnect()
    print("Da dung device")
