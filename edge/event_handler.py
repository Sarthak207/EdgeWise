import sqlite3
from datetime import datetime, timedelta
import time
import paho.mqtt.client as mqtt

# ================================
# CONFIGURATION
# ================================
BROKER = "localhost"
PORT = 1883
TOPIC = "edgewise/sensor/motion"

DB_FILE = "edgewise.db"
ALERT_THRESHOLD = 3
ALERT_WINDOW = 10
INACTIVITY_LIMIT = 60
# ================================

motion_times = []
last_motion_time = None
system_state = "IDLE"

# ---- Database helper ----
def save_event(event_type, message=""):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute(
        "INSERT INTO motion_events (timestamp, event_type, message) VALUES (?, ?, ?)",
        (datetime.now().isoformat(), event_type, message)
    )
    conn.commit()
    conn.close()

# ---- MQTT Callbacks ----
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        client.subscribe(TOPIC)
    else:
        print(f"⚠️ Failed to connect, rc={rc}")

def on_message(client, userdata, msg):
    global last_motion_time, system_state

    payload = msg.payload.decode()
    now = datetime.now()
    print(f"[{now}] {payload}")

    # Save event to DB
    save_event("MOTION", payload)

    # Motion logic
    motion_times.append(now)
    last_motion_time = now

    # Clean up old motion timestamps
    cutoff = now - timedelta(seconds=ALERT_WINDOW)
    while motion_times and motion_times[0] < cutoff:
        motion_times.pop(0)

    # Frequent motion alert
    if len(motion_times) >= ALERT_THRESHOLD:
        print("🚨 Frequent motion detected!")
        save_event("ALERT", "Frequent motion burst")

    # State transition
    if system_state == "IDLE":
        system_state = "ACTIVE"
        print("🟢 State changed: ACTIVE")
        save_event("STATE", "ACTIVE")

def main():
    global system_state

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print("📡 Intelligent event handler (DB integrated)...\n")

    try:
        while True:
            if system_state == "ACTIVE" and last_motion_time:
                if (datetime.now() - last_motion_time).total_seconds() > INACTIVITY_LIMIT:
                    system_state = "IDLE"
                    print("⚪ State changed: IDLE")
                    save_event("STATE", "IDLE")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n🛑 Exiting gracefully.")
        client.loop_stop()

if __name__ == "__main__":
    main()




