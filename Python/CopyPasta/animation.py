from picamera import PiCamera
from time import sleep
from gpiozero import Button
import keyboard

button = keyboard.is_pressed('h')
camera = PiCamera()

while True:
	camera.start_preview()
	button.wait_for_press()
	print("Button has been pressed!")
	sleep(3)
	camera.capture('animateImage.jpg')
	camera.stop_preview()
