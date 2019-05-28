#########################################
#				Softlight				#
#########################################
# @Author: Aaron Earl					#
# 5/27/19								#
#										#
# From Freenove RPi Tutorials			#
# Ch.8 Potentiometer and LED			#
#										#
# Note: Similar wiring setup from last	#
# lab. AOUT pin is no longer connected	#
# to 220Ohm resistor and LED, instead	#
# LED and resistor are connected to		#
# GPIO 17.								#
#########################################

import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus = smbus.SMBus(1)
cmd = 0x40
ledPin = 11

def analogRead(chn):

	value = bus.read_byte_data(address, cmd + chn)
	return value

def analogWrite(value):

	bus.write_byte_data(address, cmd, value)

def setup():

	global p
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, GPIO.LOW)

	p = GPIO.PWM(ledPin, 1000)
	p.start(0)

def loop():

	while True:
		value = analogRead(0)	#Read A0 pin
		#Convert ADC value to duty cycle of PWM
		p.ChangeDutyCycle(value * 100 / 255)
		voltage = value / 255.0 * 3.3	#Calculate voltage
		print("ADC Value: %d, Voltage: %.2fV" %(value, voltage))
		time.sleep(0.01)

def destroy():

	bus.close()
	GPIO.cleanup()

if __name__ == "__main__":

	print("Program is starting")
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()

