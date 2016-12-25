#!/usr/bin/env python3

r, c, zr, zc = (int(x) for x in input().split())
mat = []

for _ in range(r):
	row = input()
	nr = ""
	for c in row:
		nr += c * zc
	for _ in range(zr):
		print(nr)
