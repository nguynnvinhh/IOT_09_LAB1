
import paho.mqtt.client as mqtt
import threading

BROKER = "broker.emqx.io"
PORT = 1883

CMD_TOPIC = "iot/lab/light01/cmd"
STATUS_TOPIC = "iot/lab/light01/status"

connected = threading.Event()


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi MQTT broker")
        client.subscribe(STATUS_TOPIC)
        connected.set()
    else:
        print("Ket noi that bai:", reason_code)


def on_message(client, userdata, msg):
    print("\nTrang thai nhan duoc:")
    print(msg.payload.decode())
    print("Nhap lenh (ON/OFF/EXIT): ", end="", flush=True)


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    if not connected.wait(timeout=10):
        print("Khong ket noi duoc MQTT broker")
    else:
        while True:
            command = input("\nNhap lenh (ON/OFF/EXIT): ").strip().upper()

            if command == "EXIT":
                break

            if command not in ("ON", "OFF"):
                print("Lenh khong hop le")
                continue

            info = client.publish(CMD_TOPIC, command, qos=1)
            info.wait_for_publish()
            print("Da gui lenh", command, "toi light01")

finally:
    client.loop_stop()
    client.disconnect()
