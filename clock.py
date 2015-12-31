#!/usr/bin/python
import sys
import time
import datetime
import clock_digits
from sense_hat import SenseHat

sense = SenseHat()      # create sense object
sense.set_rotation(180) # better when USB cable sticks out the top
sense.low_light = True  # don't hurt my eyes
sense.clear()           # always start with a clean slate

charWidth  = 4
charHeight = 4

# returns the specified row of the digit
def digitrow(digit, row):
	return digit[row * charWidth : (row * charWidth) + charWidth]

# main display routine
# takes a list of 4 digits and displays them on the LED-matrix
def display(digits):
	
	if len(digits) > 4:
		return

	x = [0, 0, 0] # off
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

	for i in range(0, len(digits)):
		charStart = offsets[i]

		for j in range(0, charHeight):

			row = digitrow(digits[i], j) # gets a sinlge row from the digit

			# calculate where current row starts
			rowStart = charStart + (j * charWidth) + (j * charWidth)
			screen[rowStart : rowStart + charWidth] = row

	sense.set_pixels( screen )

# main loop
while True:
	now     = datetime.datetime.now().time()
	str_now = str(now.hour).zfill(2) + str(now.minute).zfill(2)
	display( [
		clock_digits.digits[int(str_now[0])],
		clock_digits.digits[int(str_now[1])], 
		clock_digits.digits[int(str_now[2])], 
		clock_digits.digits[int(str_now[3])]] 
	)

	time.sleep(1)
	