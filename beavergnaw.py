#!/usr/bin/env python3

import math
line = input()
while line != "0 0":
	D, V = (int(x) for x in line.split())
	print("{0:.7f}".format((D*D*D - 6*V / math.pi) ** (1/3)))
	line = input()
