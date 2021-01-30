import time
import picamera
class picamera.camera.PiCamera(camera_num=0, stereo_mode='none', stereo_decimate=False, resolution=None, framerate=None, sensor_mode=0, led_pin=None) 
count = 0
with picamera.PiCamera() as camera:
    print("Getting ready.... say cheese!")
    camera.resolution = (1024, 768)
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
    time.sleep(2)
    camera.capture('YourPhoto.jpg')
    print("Done")

camera = PiCamera()
try:
    # do something with the camera
    pass
finally:
    camera.close()
