#############################################
#					ADC 			 		#
#############################################
# @Author: Aaron Earl						#
# 5/27/19									#
#											#
# From Freenove RPi							#
# tutorials									#
# Ch.7 AD/DA Converter						#
#											#
# Task: Convert analog output to digital	#
# voltage									#
#											#
# Note: My kit came with					#
# the PCF8591T IC chipp						#
#											#
# Pin Notes: the IC  diagram wasn't very	#
# clear so I've wrote out the pin values	#
# as follows;								#
#											#
# Left Pins									#
# AIN0: Potentiometer to Pin3 input			#
# AIN1: No input							#
# AIN2: No input							#
# AIN3: No input							#
# A0: GND									#
# A1: GND									#
# A2: GND									#
# VSS: GND									#
#											#
# Right Pins								#
# VDD: +3.3V								#
# AOUT: 220Ohm Resistor to LED				#
# VREF: +3.3V								#
# AGND: GND									#
# EXT: GND									#
# OSC: No input/output						#
# SCL: SCL1(Board)							#
# SDA: SDA1(Board)							#
#############################################

import smbus
import time

address = 0x48 #default address of PCF8591
bus = smbus.SMBus(1)
cmd = 0x40		#command

def analogRead(chn):	#read ADC value, chn: 0, 1, 2, 3

	value = bus.read_byte_data(address, cmd + chn)
	return value

def analogWrite(value):	#write DAC value

	bus.write_byte_data(address, cmd, value)

def loop():

	while True:
		value = analogRead(0)	#read the ADC value of channel 0
		analogWrite(value)		#write the DAC value
		voltage = value / 255.0 * 3.3	#calculate the voltage value
		print("ADC Value: %d, Voltage: %.2f" %(value, voltage))
		time.sleep(0.01)

def destroy():

	bus.close()

if __name__ == "__main__":

	print("Program is starting...")

	try:
		loop()
	except KeyboardInterrupt:
		destroy()



