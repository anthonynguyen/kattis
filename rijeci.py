#!/usr/bin/env python3

k = int(input())
if k == 1:
	print(0, 1)
else:
	n, a, b = 1, 1, 1
	while k - 1 > n:
		c = a + b
		a, b = b, c
		n += 1
	print(a, b)
