import time
import picamera
from datetime import datetime
#capture_continuous(output, format=None, use_video_port=False, resize=None, splitter_port=0, burst=False, **options)
val = 0
filename = "{0:%c}".format(datetime.now())
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
        camera.capture(str(val)+filename+".jpg")
        print("Done")
        val = val+1
    else:
        camera.close() 
