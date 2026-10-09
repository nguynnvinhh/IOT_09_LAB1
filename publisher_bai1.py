
import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "iot/lab/message"

NAME = "Nguyen Ngoc Vinh"
STUDENT_ID = "B23DCCN935"

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.connect(BROKER, PORT, 60)
client.loop_start()

message = (
    f"Xin chao tu client Python MQTT - "
    f"{STUDENT_ID} - {NAME}"
)

info = client.publish(TOPIC, message, qos=1)
info.wait_for_publish()

print("Da gui message:")
print("Topic:", TOPIC)
print("Payload:", message)

client.loop_stop()
client.disconnect()
