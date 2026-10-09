
import json
import random
import time
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"
PORT = 1883
TOPIC = "iot/lab/sensor/data"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        for device in ("sensor01", "sensor02"):
            data = {
                "device_id": device,
                "temperature": round(random.uniform(25, 40), 1),
                "humidity": round(random.uniform(30, 80), 1)
            }

            payload = json.dumps(data)
            info = client.publish(TOPIC, payload, qos=1)
            info.wait_for_publish()
            print("Da gui:", payload)

        time.sleep(3)

except KeyboardInterrupt:
    print("\nDa dung Sensor Publisher")
finally:
    client.loop_stop()
    client.disconnect()
