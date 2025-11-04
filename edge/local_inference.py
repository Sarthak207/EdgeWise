import cv2
import psutil
from ultralytics import YOLO
import time

model= YOLO("yolov8n.pt")

frame= cv2.imread("sample.jpg")
if frame is None:
	raise FileNotFoundError("Could not find sample.jpg")

def get_system_status():
	cpu= psutil.cpu_percent(interval=1)
	temp=0
	try:
		with open("/sys/class/thermal/thermal_zone0/temp") as f:
			temp= int(f.read())/ 1000.0
	except:
		pass
	return cpu,temp

cpu,temp= get_system_status()
print(f"Starting local inference | CPU {cpu:.1f}% | Temp {temp:.1f}C")

start= time.time()
results= model(frame)
end= time.time()

#results[0].show()
print(f"Inference complete in {end-start:.2f}s")
print("Detections:", results[0].to_json())
