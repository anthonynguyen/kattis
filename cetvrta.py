#!/usr/bin/env python3

x = []
y = []
points = []
for _ in range(3):
	xx, yy = (int(x) for x in input().split())
	x.append(xx)
	y.append(yy)
	points.append((xx, yy))
for xx in x:
	for yy in y:
		if (xx, yy) not in points:
			print(xx, yy)
