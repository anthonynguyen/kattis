#!/usr/bin/env python3

a = 1
b = 0
c = 0

for m in input():
	if m == "A":
		a, b = b, a
	elif m == "B":
		b, c = c, b
	elif m == "C":
		a, c = c, a

if a:
	print("1")
elif b:
	print("2")
elif c:
	print('3')
