# 🔬 Edge-Aware Adaptive Vision System  
### _Intelligent Inference Offloading for Energy-Efficient IoT Vision_

---

## 🧠 Overview
This project demonstrates an **adaptive edge–cloud collaboration system** for computer vision tasks.  
It combines an **Raspberry Pi 4B (edge)** and **ESP8266 nodes (sensor network)** to build a **smart vision pipeline** that dynamically decides **where to run inference** — locally on the Pi or remotely on the cloud — based on **real-time factors** like CPU load, network latency, and battery level.

---

## 🎯 Motivation
In traditional IoT systems, all vision tasks are either:
- Processed **locally**, causing **high power consumption**, or
- **Offloaded to the cloud**, leading to **latency and privacy concerns**.

This project proposes a **hybrid decision layer** that intelligently selects the optimal computation location for every frame — making inference both **efficient and adaptive**.

---

## ⚙️ System Architecture
[ESP8266 Sensor Nodes] ---> [Raspberry Pi 4B (Edge Controller)]
|
[Local YOLO-NAS Quantized Model]
|
[Cloud Inference Server (FastAPI)]

yaml
Copy code

1. **ESP8266 Nodes:**  
   Detect motion, temperature, or sound anomalies and notify the RPi via MQTT/Wi-Fi.

2. **Raspberry Pi 4B:**  
   Acts as the **edge gateway**, captures frames, and decides where inference runs:
   - Run locally if CPU load < threshold.
   - Offload to cloud if latency or thermal limits are exceeded.

3. **Cloud Inference Server:**  
   Hosts the **YOLOv8/YOLO-NAS** model (full precision).  
   Returns inference results via REST API.

---

## 🧩 Core Components

| Component | Role | Implementation |
|------------|------|----------------|
| **ESP8266 Node** | Trigger event (motion, sound, light) | Arduino / MicroPython |
| **MQTT Broker** | Communication layer | Mosquitto on RPi |
| **Raspberry Pi** | Edge inference + adaptive logic | Python + OpenCV + psutil |
| **Cloud Server** | Full-scale model inference | FastAPI + YOLOv8 |
| **Database (Optional)** | Store inference results & stats | SQLite / Supabase |

---

## ⚡ Key Features
- 🧠 **Adaptive Offloading:** Dynamically choose edge or cloud inference.  
- 🔋 **Energy Awareness:** Monitor CPU load, temperature, and network speed.  
- ☁️ **Cloud Integration:** Seamless REST-based model inference.  
- 🧩 **Modular Design:** Works with any sensor or model backend.  
- 📊 **Performance Logging:** Tracks FPS, latency, and energy usage for research metrics.

---

## 🧪 Research Value
- Studies **energy–latency trade-offs** in edge computing.
- Implements **dynamic decision algorithms** for real-time inference offloading.
- Can serve as a base for papers in:
  - Adaptive Edge Computing
  - Federated/Collaborative IoT
  - Energy-Efficient AI at the Edge

---

## 🛠️ Tech Stack
| Layer | Tools / Frameworks |
|-------|---------------------|
| Edge | Python, OpenCV, psutil, MQTT |
| Cloud | FastAPI, Ultralytics YOLOv8, Flask, ngrok |
| Communication | MQTT / HTTP REST |
| Hardware | Raspberry Pi 4B, ESP8266, USB Camera |
| Sensors | PIR, DHT11/22, Sound Sensor (any optional) |

---

## 🚀 Setup Roadmap (Step-by-Step)
### Phase 1: Hardware Setup
- [ ] Configure ESP8266 with sensor + Wi-Fi.
- [ ] Setup MQTT broker on RPi.

### Phase 2: Edge Processing
- [ ] Capture camera frames.
- [ ] Run local inference using quantized YOLO-NAS.
- [ ] Log CPU load, FPS, and latency.

### Phase 3: Cloud Inference
- [ ] Deploy FastAPI server with full YOLO model.
- [ ] Receive frames and return detections.

### Phase 4: Adaptive Logic
- [ ] Write Python script to auto-switch inference mode.
- [ ] Implement thresholds and dynamic decision-making.

### Phase 5: Performance Evaluation
- [ ] Compare latency, FPS, and power draw.
- [ ] Visualize trade-offs in a dashboard.

---

## 📈 Future Scope
- Integrate **reinforcement learning** to optimize decision thresholds.
- Expand to **multi-node edge collaboration**.
- Add **blockchain-based trust layer** for secure inference logs.

---

## 👨‍💻 Author
**Sarthak Pardeshi**  
IoT | Computer Vision | Edge AI Research Enthusiast  

---
