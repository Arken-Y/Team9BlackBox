from time import sleep
import picamera
import datetime

system_time = datetime.datetime.now()
camera = picamera.PiCamera()
camera.resolution = (640, 480)
a = ".h264"
b = str(system_time) + a

user_input = input("Start Record? (Y/N)")
if(user_input == "Y" or user_input.lower() == "y"):
    camera.start_preview()
    camera.preview_alpha = 255
    camera.preview_fullscreen = False
    camera.preview_window = (0, 0, 640, 480)
    camera.start_recording(b)
    
    user_stop_input = input("Stop Record? (Y/N)")
    if(user_stop_input != "N"):
            camera.stop_recording()
            camera.stop_preview()
            

#camera.wait_recording(5)
