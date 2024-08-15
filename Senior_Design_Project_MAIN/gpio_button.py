import time
import RPi.GPIO as GPIO
import subprocess
from time import sleep
import signal

#time.sleep(5)
def button_callback1(channel):
    process1 = subprocess.Popen(["sh", "/home/pi/Desktop/Senior_Design_Project/start.sh"])
    #print("Press1")

def button_callback2(channel):
    #print("Press2")
    process2 = subprocess.Popen(["sh", "/home/pi/Desktop/Senior_Design_Project/stop.sh"])
    print("Process Quit!")
  
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(11,GPIO.RISING,callback=button_callback1)
GPIO.add_event_detect(13,GPIO.RISING,callback=button_callback2)
 # Setup event on pin 10 rising edge
#count = 0
"""
while True:
    count += 1
    if GPIO.input(11):
        #GPIO.add_event_detect(11,GPIO.RISING,callback=button_callback1)
        print("Press1")
    if GPIO.input(13):
        #GPIO.add_event_detect(13,GPIO.RISING,callback=button_callback2)
        print("Press2")


#message = input()
#message = input("Press enter to quit\n\n")# Run until someone presses enter
while True:
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)"""
signal.pause()
GPIO.cleanup() # Clean up
