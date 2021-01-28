# Here is where I will write my code for the headless assignment
import time
import gc
import math
#import framebuf

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
	e = (11-abs(x2))*2.0454545454545
	f = (11-abs(y))*2.0454545454545
	g = (11-abs(z))*2.0454545454545
	print(x2,y,z)
	time.sleep(0.5)
	# Get drawing object to draw on image.
	draw = ImageDraw.Draw(image)
	# Draw a black filled box to clear the image.
	draw.rectangle((0,0,width,height), outline=0, fill=0)
	# First define some constants to allow easy resizing of shapes.
	padding = 5
	xpadding = 25
	shape_width = 20
	top = padding
	topx = padding+e
	topy = padding+f
	topz = padding+g
	bottom = height-padding-9
	# Move left to right keeping track of the current x position for drawing shapes.
	x = padding
	# Load default font.
	font = ImageFont.load_default()
	# +45 =   -11
	# +0  =    11
	# +22.5   = 0
	draw.text((x, top + 35), '___________________', font=font, fill=255)
	draw.text((x, top + 45), ' x       y      z', font=font, fill=255)
	# Draw a bar for each variable
	draw.rectangle((x, topx, x+shape_width, bottom), outline=255, fill=255)
	x += shape_width+xpadding
	draw.rectangle((x, topy, x+shape_width, bottom), outline=255, fill=255)
	x += shape_width+xpadding
	draw.rectangle((x, topz, x+shape_width, bottom), outline=255, fill=255)
	# Display Image
	disp.image(image)
	disp.display()

