import time
import RPi.GPIO as GPIO
import os

GPIO .setmode(GPIO.BCM)
switch1 = 27
led1 = 13
led2 = 12
switch2 = 16
press_time = 0
press_count = 0

GPIO.setup(switch1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led2, GPIO.OUT, initial=GPIO.HIGH)

def button1(pin):
    global press_time
    global press_count
    GPIO.output(led1, GPIO.input(switch1))
    if GPIO.input(switch1) == 0:
        while not GPIO.input(switch1):
            press_time = press_time + 1
            time.sleep(1)
            
    if GPIO.input(switch1) == 1:
        press_count = press_time
        os.system ("cat /proc/vmstat")
        press_time = 0
        print("end")
        
def button2(pin):
    global press_time
    global press_count
    GPIO.output(led2, GPIO.input(switch2))
    if GPIO.input(switch2) == 0:
        while not GPIO.input(switch2):
            GPIO.output(led2,0)
            time.sleep(.2)
            GPIO.output(led2, 1)
            time.sleep(.2)
            GPIO.output(led2,0)
            time.sleep(.2)
            GPIO.output(led2, 1)
            time.sleep(.2)
            press_time = press_time + 1
          
            
    if GPIO.input(switch2) == 1:
        press_count = press_time
        press_time = 0


GPIO.add_event_detect(switch1, GPIO.BOTH, button1)
GPIO.add_event_detect(switch2, GPIO.BOTH, button2)
while 1 == 1 :
    if press_count > 0:
        print (press_count)
        press_count = 0
   

