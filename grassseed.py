#!/usr/bin/env python3

c = float(input())
l = int(input())
t = 0
for _ in range(l):
	p = input().split()
	w, h = float(p[0]), float(p[1])
	t += w * h * c
print("{0:.7f}".format(t))
