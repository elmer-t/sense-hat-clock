#!/usr/bin/python
import sys
import time
import datetime
import clock_digits

from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True
sense.clear()

x = [0, 0, 0] # off
o = [255, 255, 255] # on

charWidth  = 4
charHeight = 4

# returns the specified row of the digit
def digitrow(digit, row):
	return digit[row * charWidth : (row * charWidth) + charWidth]

def display(digits):
	
	if len(digits) > 4:
		return

	screen = [
		x, x, x, x, x, x, x, x,
		x, x, x, x, x, x, x, x,
		x, x, x, x, x, x, x, x,
		x, x, x, x, x, x, x, x,
		x, x, x, x, x, x, x, x,
		x, x, x, x, x, x, x, x,
		x, x, x, x, x, x, x, x,
		x, x, x, x, x, x, x, x,
	]

	offsets = [0, 4, 32, 36] # positions where chars start
	spacing = 4 # nr of LEDs to skip until next row

	for i in range(0, len(digits)):
		charStart = offsets[i]

		for j in range(0, charHeight):

			row = digitrow(digits[i], j) # gets a sinlge row from the digit

			# calculate where current row starts
			rowStart = charStart + (j * charWidth) + (j * spacing)
			screen[rowStart : rowStart + charWidth] = row

	sense.set_pixels( screen )


while True:
	now   = datetime.datetime.now().time()
	str_now = str(now.hour).zfill(2) + str(now.minute).zfill(2)
	display( [
		clock_digits.digits[int(str_now[0])],
		clock_digits.digits[int(str_now[1])], 
		clock_digits.digits[int(str_now[2])], 
		clock_digits.digits[int(str_now[3])]] 
	)

	time.sleep(1)
	
