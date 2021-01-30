import gpiozero
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_Pin = 4
GPIO.setup(PIR_Pin, GPIO.IN)

try:
        print ("PIR Module Test (CTRL+C to exit)")
        time.sleep(2)
        print ("Ready")
        while True:
            if GPIO.input(PIR_Pin):
                print ("Motion Detected!")
                time.sleep(1)
except KeyboardInterrupt:
        print ("Quit")
        GPIO.cleanup()


