#!/usr/bin/env python3

n = int(input())
while n != -1:
	cases = int(n)
	d = 0
	e = 0
	for i in range(cases):
		segment = input().split()
		speed, elapsed = int(segment[0]), int(segment[1])
		d += speed * (elapsed - e)
		e = elapsed
	print(d, "miles")
	n = int(input())
