#!/usr/bin/env python3

import math

def t(v0, theta, x):
	return x / v0 / math.cos(math.radians(theta))

def y(v0, theta, t):
	return v0 * t * math.sin(math.radians(theta)) - 0.5 * 9.81 * t * t

for _ in range(int(input())):
	v0, theta, x1, h1, h2 = (float(i) for i in input().split())
	t1 = t(v0, theta, x1)
	y1 = y(v0, theta, t1)
	if y1 < h2 - 1 and y1 > h1 + 1:
		print("Safe")
	else:
		print("Not Safe")
