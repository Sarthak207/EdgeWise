from flask import Flask, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import time

app = Flask(__name__)

# Load YOLO model (quantized version is ideal for Pi)
model = YOLO("yolov8n.pt")

@app.route('/')
def home():
    return jsonify({"status": "Flask Inference Server Running"})

@app.route('/infer', methods=['POST'])
def infer():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    # Read the uploaded image
    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    # Run inference
    start = time.time()
    results = model(frame)
    end = time.time()

    result_json = results[0].to_json()
    print(f"Inference complete in {end - start:.2f}s")

    return jsonify({
        "status": "success",
        "inference_time": round(end - start, 2),
        "detections": result_json
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

