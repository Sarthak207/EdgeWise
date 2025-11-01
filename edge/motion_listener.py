import paho.mqtt.client as mqtt
from datetime import datetime

# === MQTT CONFIG ===
MQTT_BROKER = "localhost"   # same Pi running mosquitto
MQTT_PORT = 1883
MQTT_TOPIC = "edgewise/sensor/motion"

# === MQTT CALLBACKS ===
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT broker")
        client.subscribe(MQTT_TOPIC)
        print(f"📡 Subscribed to topic: {MQTT_TOPIC}")
    else:
        print("❌ Connection failed with code", rc)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"\n📨 Received message: {message} at {datetime.now().strftime('%H:%M:%S')}")
    if message == "MOTION_DETECTED":
        print("⚡ Motion detected! (Trigger decision module here later)")
        # Future camera logic goes here
        # capture_and_process_frame()
        
# === SETUP MQTT CLIENT ===
client = mqtt.Client("pi_motion_listener")
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()


