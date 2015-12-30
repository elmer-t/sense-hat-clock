
import random

x = [0, 0, 0] # off
#o = [255, 255, 255] # on

def o():
	return [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

digits = [
	[ # zero
		x, x, x, x,
		x, o(), o(), o(),
		x, o(), x, o(),
		x, o(), o(), o(),
	],
	[ # one
		x, o(), o(), x,
		x, x, o(), x,
		x, x, o(), x,
		x, x, o(), x,
	],
	[ # two
		x, o(), o(), o(),
		x, x, x, o(),
		x, x, o(), x,
		x, o(), o(), o(),
	],
	[ # three
		x, o(), o(), o(),
		x, x, x, o(),
		x, x, o(), o(),
		x, o(), o(), o(),
	],
	[ # four
		x, x, x, o(),
		x, o(), x, o(),
		x, o(), o(), o(),
		x, x, x, o(),
	],
	[ # five
		x, o(), o(), o(),
		x, o(), o(), x,
		x, x, x, o(),
		x, o(), o(), o(),
	],
	[ # six
		x, o(), x, x,
		x, o(), o(), o(),
		x, o(), x, o(),
		x, o(), o(), o(),
	],
	[ # seven
		x, o(), o(), o(),
		x, x, x, o(),
		x, x, x, o(),
		x, x, x, o(),
	],
	[ # eight
		x, x, o(), x,
		x, o(), o(), o(),
		x, o(), o(), o(),
		x, x, o(), x,
	],
	[ # nine
		x, o(), o(), o(),
		x, o(), x, o(),
		x, o(), o(), o(),
		x, x, x, o(),
	],
]
