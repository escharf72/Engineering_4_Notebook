# Here is the file for the code that I will be writing/compiling for the gpioI2C assignment
# Author: Tony DiCola
# License: Public Domain
import time
#Library for the accelerometer 
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# Library for the screen
import Adafruit_LSM303
# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()
# Alternatively you can specify the I2C bus with a bus parameter:
#lsm303 = Adafruit_LSM303.LSM303(busum=2)
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d) 
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
	# Read the X, Y, Z axis acceleration values and print them.
	accel, mag = lsm303.read()
	# Grab the X, Y, Z components from the reading and print them out.
	accel_x, accel_y, accel_z = accel
	x2  = round(accel_x / 100, 5)
	y = round(accel_y / 100, 4)
	z = round(accel_z / 100, 3)
	print(x2,y,z) 
	#mag_x, mag_y, mag_z = mag
	#print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
	# Wait half a second and repeat.
	time.sleep(0.5)
	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)
	# Draw a black filled box to clear the image.
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	# First define some constants to allow easy resizing of shapes.
	padding = 2
	shape_width = 20
	top = padding
	bottom = height-padding
	# Move left to right keeping track of the current x position for drawing shapes.
	x = padding
	# Load default font.
	font = ImageFont.load_default()
	# Write out variables on the screen
	draw.text((x, top), 'Accel Data:', font=font, fill=255)
	draw.text((x, top+16), 'x ={0}'.format(x2), font=font, fill=255)
	draw.text((x, top+30), 'y ={0}'.format(y), font=font, fill=255)
	draw.text((x, top+45), 'z ={0}'.format(z), font=font, fill=255)
	# Display image.
	disp.image(image)
	disp.display()
