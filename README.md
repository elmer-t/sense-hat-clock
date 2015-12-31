# Raspberry Pi + Sense HAT clock
A small project to display to current time on a Raspberry Pi + Sense HAT

The Sense HAT is an add-on board for Raspberry Pi, made especially for the Astro Pi mission – it’s going to the International Space Station in December 2015. The Sense HAT has an 8×8 RGB LED matrix, a five-button joystick and includes the miscellaneous sensors.

For this project I'm only using the LED matrix.

## Display
Displaying 4 digits on an 8×8 matrix is a bit of a challenge. Each digit only has 4×4 LEDs and there needs to be some space between individual digits. This effectively leaves 3×4 LEDs per digit. For some digits this work fine, for some not so. The 3, 5 and 8 are especially difficult, as is distinguishing between 0 and 8.

Have a look in clock_digits.py to see what I've come up with.

I initially started with plain white digits, but this proved to be too bright. After experimenting a bit with (random) colors, I settled for red. This has the advantage of looking good when placing a piece of red acrylic plastic over the display.

![alt tag](https://raw.githubusercontent.com/elmer-t/sense-hat-clock/master/img/IMG_5225.JPG)
