#################################################
#				ColorfulSoftlight				#
#################################################
# @Author: Aaron Earl							#
# 5/27/19										#
#												#
# From Freenove RPi Tutorials					#
# Ch.9 Potentiometer and RGBLED					#
#												#
# Note: Circuit setup is similar to last lab.	#
# Pins AIN1 and AIN2 are connected to a			#
# potentiometer.								#
#################################################

import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40

#Define the 3 pins of the RGBLED
ledRedPin = 15
ledGreenPin = 13
ledBluePin = 11

def analogRead(chn):	#Read ADC value

	bus.write_byte(address, cmd + chn)
	value = bus.read_byte(address)
	value = bus.read_byte(address)
	#Note: This function always returns the last data read,
	#if you want to return the current data, you need to execute it twice

	return value

def analogWrite(value):

	bus.write_byte_data(address, cmd, value)

def setup():

	global p_Red, p_Green, p_Blue

	#Set three pins of the RGBLED to output mode
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledRedPin, GPIO.OUT)
	GPIO.setup(ledGreenPin, GPIO.OUT)
	GPIO.setup(ledBluePin, GPIO.OUT)

	#Configure PWM to the 3 pins of RGBLED
	p_Red = GPIO.PWM(ledRedPin, 1000)
	p_Red.start(0)
	p_Green = GPIO.PWM(ledGreenPin, 1000)
	p_Green.start(0)
	p_Blue = GPIO.PWM(ledBluePin, 1000)
	p_Blue.start(0)


def loop():

	while True:
		#Read the ADC values of the three potentiometers
		value_Red = analogRead(0)
		value_Green = analogRead(1)
		value_Blue = analogRead(2)

		#Map the read value of the potentiometers into PWM value and output
		p_Red.ChangeDutyCycle(value_Red * 100 / 255)
		p_Green.ChangeDutyCycle(value_Green * 100 / 255)
		p_Blue.ChangeDutyCycle(value_Blue * 100 / 255)

		#Print read ADC values
		print("ADC Values value_Red: %d, \tvalue_Green: %d, \tvalue_Blue: %d"
		%(value_Red, value_Green, value_Blue))

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
