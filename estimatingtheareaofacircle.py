#!/usr/bin/env python3

import math
line = input()
while line != "0 0 0":
	p = line.split()
	r, m, c = float(p[0]), int(p[1]), int(p[2])
	print(math.pi * r * r, 4 * r * r * c / m)
	line = input()
