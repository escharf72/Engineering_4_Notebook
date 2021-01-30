import time
import picamera
count = 0
with picamera.PiCamera() as camera:
    #while count <= 4:
    print("Getting ready.... say cheese!")
    camera.resolution = (1024, 768)
    camera.start_preview()
    for effect in camera.IMAGE_EFFECTS:
        camera.image_effect = effect
        camera.annotate_text = "Effect: %s" % effect
        #time.sleep(5)
    #camera.stop_preview()
       # while count == 0:
        #        camera.image_effect = 'oilpaint'
        #while count == 1:
         #       camera.image_effect = 'pastel'
        #while count == 2:
        #        camera.image_effect = 'cartoon'
        #while count == 3:
        #        camera.image_effect = 'watercolor'
        #while count == 4: 
         #       camera.image_effect = 'solarize'
       # camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture('YourPhoto.jpg')
        #count = count + 1
#else:
    #print("Done!")
    #exit()

