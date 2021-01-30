import time
import picamera
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
