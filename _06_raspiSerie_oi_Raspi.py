#!/usr/bin/env python

# File          _06_raspiSerie_oi_Raspi.py
# Project:      #raspiSerie-06 Raspberry Pi Ripple Board w/ PCF8591P
# Description:  Turn on & off led on GPIO.24 using button on GPIO.4
# Youtube:      http://goo.gl/unfHZA
# G+/j3:        http://goo.gl/FOZblH
# Run:          sudo phyton io_rasp.py
# Stop:         CTRL+C
# Date:         sept-2016
# Software: 	  2016-05-27-raspian-jessie
#   		        Python 2.7.9
#---------------------------------------------------------------------------------
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License v3 as published by
#  the Free Software Foundation
#---------------------------------------------------------------------------------
import RPi.GPIO as GPIO
from time import sleep     # this lets us have a time delay (see line 12)
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
#GPIO.setup(4, GPIO.IN)    # set GPIO4 as input (button) with pull-down & up
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # need pull-up only
GPIO.setup(25, GPIO.OUT)   # set GPIO25 as an output (LED)

try:
    while True:            # this will carry on until you hit CTRL+C
        if GPIO.input(4):  # if port 25 == 1
            print "Port 4 is 1/HIGH/True - LED ON"
            GPIO.output(25, 1)  # set port/pin value to 1/HIGH/True
        else:
            print "Port 4 is 0/LOW/False - LED OFF"
            GPIO.output(25, 0)  # set port/pin value to 0/LOW/False
        sleep(0.1)         # wait 0.1 seconds

finally:                   #  run no matter how the try block exits
    GPIO.cleanup()
