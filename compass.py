#!/usr/bin/env python3

cur = int(input())
correct = int(input())

d = correct - cur
if d < -180:
	d += 360
elif d > 180:
	d -= 360
if d == -180:
	d = 180
print(d)
