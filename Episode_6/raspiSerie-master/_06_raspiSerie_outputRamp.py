#!/usr/bin/env python

# Project:        #raspiSerie-06 Raspberry Pi Ripple Board w/ PCF8591P
# File: 	        _06_raspiSerie_outputRamp.py
# Description: 	  This simply reads the voltage value on anolog input channel 0 and 
#                 prints it out if it has changed; 1ª raw - A/D converter reading
#                 and the 2ª raw what it means in terms of volts#
# Youtube:  	    http://goo.gl/unfHZA 
# G+/j3:	        http://goo.gl/FOZblH
#
# Run: 		        sudo phyton hello1.py or sudo python3 hello1.py
# Stop: 	        CTRL+C
# Date: 	        sept-2016
# Software: 	    2016-05-27-raspian-jessie
#  		            Python 2.7.9
#---------------------------------------------------------------------------------
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License v3 as published by
#  the Free Software Foundation
#---------------------------------------------------------------------------------

# Output a count to the D/A in the PCF8591P @ address 74 
from smbus import SMBus
from time import sleep

# comment out the one that does not apply to your board
# bus = SMBus(0) 			# For revision 1 boards
bus = SMBus(1) 				# For revision 2 boards

address = 74				# Address connections: A0=LOW; A1=HIGH; A2=LOW

control = 1<<6 				# Enable analog output by setting bit 6

print "Output a ramp on the D/A" 

print "Ctrl C to stop" 

while True:
	for a in range(0,256):
		bus.write_byte_data(address, control, a) # output to D/A
		sleep(0.01)
