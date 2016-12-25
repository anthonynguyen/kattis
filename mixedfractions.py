#!/usr/bin/env python3

import fractions
line = input()
while line != "0 0":
	n, d = (int(x) for x in line.split())
	print("{} {} / {}".format(n // d, n % d, d))
	line = input()
