#!/usr/bin/env python3

cipher = input()
d = 0
for i, l in enumerate(cipher):
	if i % 3 == 0 and l != "P" or i % 3 == 1 and l != "E" or i % 3 == 2 and l != "R":
		d += 1
print(d)
