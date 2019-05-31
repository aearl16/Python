#########################################
#				Thermometer				#
#########################################
# @Author: Aaron Earl					#
# 5/30/19								#
#										#
# From Freenove RPi tutorials			#
# Ch.11 Thermistor						#
#										#
# Note: Circuit setup is exactly the	#
# as the previous lab. AIN0 is			#
# instead connected to a thermistor		#
# instead of the photoresistor			#
#########################################

import RPi.GPIO as GPIO
import smbus
import time
import math

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40

def analogRead(chn):

	value = bus.read_byte_data(address, cmd + chn)
	return value

def analogWrite(value):

	bus.write_byte_data(address, cmd, value)

def setup():

	GPIO.setmode(GPIO.BOARD)

def loop():

	while True:

		value = analogRead(0) #read A0 pin
		voltage = value / 255.0 * 3.3 #Calculate voltage
		#Calculate resistanvce value of thermistor
		Rt = 10 * voltage / (3.3 - voltage)
		#Calculate temperature (Kelvin)
		tempK = 1 / (1 / (273.15 + 25) + math.log(Rt / 10) / 3950.0)
		#Calculate temperature (Celsius)
		tempC = tempK - 273.15

		print("ADC Value: %d, Voltage: %.2fV, Temperature: %.2fC"
		%(value, voltage, tempC))
		time.sleep(0.01)

def destroy():

	GPIO.cleanup()

if __name__ == "__main__":

	print("Program is starting...")

	try:
		loop()
	except KeyboardInterrupt:
		destroy()
