import RPi.GPIO as GPIO
import time

green = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT)

while True:
	GPIO.output(green, GPIO.HIGH)
	print("LED on!")
	time.sleep(.2)
	GPIO.output(green, GPIO.LOW)
	exit()
	#else: 
		#print("Program Complete!")
		#GPIO.cleanup()
		#exit()
