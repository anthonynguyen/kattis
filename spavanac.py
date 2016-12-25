#!/usr/bin/env python3

hm = input().split()
h, m = int(hm[0]), int(hm[1])

if m < 45:
	h -= 1
	m += 15
	if h < 0:
		h = 23
else:
	m -= 45

print(h, m)
