import time
import picamera
#class picamera.camera.PiCamera(camera_num=0, stereo_mode='none', stereo_decimate=False, resolution=None, framerate=None, sensor_mode=0, led_pin=None) 
val = 0
with picamera.PiCamera() as camera:
    effects = ['watercolor', 'cartoon', 'oilpaint', 'film', 'pastel']
    while val <= 4:
        print("Getting ready.... say cheese!")
        camera.resolution = (1024, 768)
        camera.start_preview()
        x = effects[val]
        camera.image_effect = x
        camera.annotate_text = x 
        time.sleep(2)
        camera.capture('Image'+str(val)+'.jpg')
        print("Done")
        val = val+1
    else:
        camera.close() 
