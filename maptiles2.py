#!/usr/bin/env python3

qk = input()
quads = [[0, 0], [1, 0], [0, 1], [1, 1]]
x, y = 0, 0
for i, c in enumerate(qk[::-1]):
	x += (2 ** i) * quads[int(c)][0]
	y += (2 ** i) * quads[int(c)][1]
print(len(qk), x, y)
