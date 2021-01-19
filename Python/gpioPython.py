import RPi.GPIO as GPIO
import time

green = 12
red = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

while True:
	GPIO.output(green, GPIO.HIGH)
	#print("LED on!")
	time.sleep(.5)
	GPIO.output(green, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(red, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(red, GPIO.LOW)
	exit()

