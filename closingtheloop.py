#!/usr/bin/env python3

for c in range(int(input())):
	input()
	segs = input().split()
	red = sorted([int(x[:-1]) for x in segs if x[-1] == "R"], reverse = True)
	blue = sorted([int(x[:-1]) for x in segs if x[-1] == "B"], reverse = True)
	if red and blue:
		l = min(len(red), len(blue))
		loop = sum(red[:l]) + sum(blue[:l]) - l - l
	else:
		loop = 0
	print("Case #{}: {}".format(c + 1, loop))
