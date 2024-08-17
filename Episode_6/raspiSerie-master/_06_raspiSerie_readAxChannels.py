#!/usr/bin/env python

# File          _06_raspiSerie_readAxChannels.py
# Project:      #raspiSerie-06 Raspberry Pi Ripple Board w/ PCF8591P
# Description:  Read a value from analog input from 0, 1 2 and 3 & print volts on console.
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
#
# in A/D in the PCF8591P @ address 74
from smbus import SMBus
# comment out the one that does not apply to your board
#bus = SMBus(0)                 # for revision 1 boards
bus = SMBus(1)                  # for revision 2 boards

address = 74

Vref = 5.0

convert = Vref / 256

print("Read the A/D channels")
print("print reading when it changes")
print("Ctrl C to stop")

i = 0

while True: # do forever

        for i in range(0,4):

                bus.write_byte(address, i) # set control register to read channel 0

                last_reading =-1

                reading = bus.read_byte(address) # read A/D 0

                if(abs(last_reading - reading) > 1): # only print on a change

                        print i, "A/D reading", reading ," meaning ", round(convert * reading,2) ,"V"

                last_reading = reading
