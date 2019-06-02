#########################################
#				Joystick				#
#########################################
# @Author: Aaron Earl					#
# 6/1/19								#
#										#
# From Freenove RPi tutorials			#
# Ch.12 Joystick						#
#										#
# Note: Circuit is the same from the	#
# last lab. AIN0 is connected to		#
# joystick VRY pin and AIN1 is			#
# connected to VRX pin.					#
#										#
# Note 2: There were several mistakes	#
# in the tutorial code. The only lines	#
# that should be in analogRead are:		#
# value =								#
# bus.read_byte_data(address, cmd + chn)#
# and return value						#
#										#
#########################################

import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
Z_Pin = 12 #Define pin for Z

def analogRead(chn): #read ADC value

	value = bus.read_byte_data(address, cmd + chn)
	return value

def analogWrite(value):

	bus.write_byte_data(address, cmd, value)

def setup():

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(Z_Pin, GPIO.IN, GPIO.PUD_UP) #set Z_Pin to pull-up mode

def loop():

	while True:

		val_Z = GPIO.input(Z_Pin) #read digital value of z
		val_Y = analogRead(0) #read analog value of X and Y
		val_X = analogRead(1)

		print("val_X: %d, \tval_Y: %d, \tval_Z: %d"
		%(val_X, val_Y, val_Z))
		time.sleep(0.01)

def destroy():

	bus.close()
	GPIO.cleanup()

if __name__ == "__main__":

	print("Program is starting...")

	setup()

	try:
		loop()
	except KeyboardInterrupt:
		destroy()
