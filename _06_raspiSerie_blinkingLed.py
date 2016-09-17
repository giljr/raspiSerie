#!/usr/bin/env python

# Project:      #raspiSerie-06 Raspberry Pi Ripple Board w/ PCF8591P
# File: 	_06_raspiSerie_blinkingLed.py
# Description: 	Turn on & off led on GPIO.24
# Youtube:  	http://goo.gl/unfHZA 
# G+/j3:	http://goo.gl/FOZblH
# Run: 		sudo phyton hello1.py or sudo python3 hello1.py
# Stop: 	CTRL+C
# Date: 	sept-2016
# Software: 	2016-05-27-raspian-jessie
   		Python 2.7.9
#---------------------------------------------------------------------------------
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License v3 as published by
#  the Free Software Foundation
#---------------------------------------------------------------------------------

try:
        from time import sleep
        import RPi.GPIO as GPIO

        GPIO.setmode(GPIO.BCM)  	   # set board mode to Broadcom
#       GPIO. setwarnings(False)

        GPIO.setup(24, GPIO.OUT)           # set up pin 24
#       GPIO.setup(25, GPIO.OUT)           # set up pin 25
        while True:
                GPIO.output(24, GPIO.HIGH) # turn on pin 24
#		GPIO.output(25, GPIO.LOW) # turn off pin 25
                sleep(1)
                GPIO.output(24, GPIO.LOW)  # turn off pin 24
#		GPIO.output(25, GPIO.HIGH) # turn on pin 24
                sleep(1)

except KeyboardInterrupt:
         GPIO.cleanup()


