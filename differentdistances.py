#!/usr/bin/env python3

def pn(p, a, b):
	return (abs(a[0] - b[0])**p + abs(a[1] - b[1])**p)**(1/p)

line = input()
while line != "0":
	a = [0, 0]
	b = [0, 0]
	a[0], a[1], b[0], b[1], p = (float(x) for x in line.split())
	print(pn(p, a, b))
	line = input()
