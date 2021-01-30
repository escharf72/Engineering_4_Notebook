from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import time 

pir = MotionSensor(4)
camera = PiCamera()
camera.resolution = (1024, 768)
filename = "{0:%c}".format(datetime.now())
 
while True:
	pir.wait_for_motion()
	#print("Motion detected!")
	camera.start_recording("video"+filename+".h264")
	#print("Recording...")
	print(filename)
	time.sleep(1)
	pir.wait_for_no_motion()
	#print("No motion detected!")
	camera.stop_recording()


