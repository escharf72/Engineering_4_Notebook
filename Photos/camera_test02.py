import time
import picamera
count = 0
0 = 'oilpaint'
1 = 'pastel'
2 = 'cartoon'
3 = 'watercolor'
4 = 'solarize'
with picamera.PiCamera() as camera:
    while count <= 4:
        print("Getting ready.... say cheese!")
        camera.resolution = (1024, 768)
        camera.image_effect(count)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('YourPhoto.jpg')
    else:
        print("Done!")
        exit()

