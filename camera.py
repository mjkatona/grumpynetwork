#!/usr/bin/python2.7
# https://picamera.readthedocs.io/en/release-1.13/
# This will take photos and light the cops

import picamera
import time
import RPi.GPIO as GPIO
import police
import threading

# Setup
police.setup()
camera = picamera.PiCamera()
camera.start_preview()
# camera.brightness = 70
camera.annotate_text_size = 60


# Variable
path = '/share/glitch/robot/'

# Funcation

def picture():
	camera.annotate_text = time.strftime("%Y%m%d-%H%M%S")
	threading.Thread(target=camera.capture(path + time.strftime("%Y%m%d-%H%M%S") + '.jpg')).start()

if __name__ == '__main__':
	picture()
	threading.Thread(target=police.police, args=(5,)).start()
	picture()
	camera.stop_preview()

