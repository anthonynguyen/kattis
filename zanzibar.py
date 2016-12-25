#!/usr/bin/env python3

for _ in range(int(input())):
	ts = [int(x) for x in input().split()][:-1]
	imp = 0
	for i, t in enumerate(ts[:-1]):
		if ts[i+1] - t * 2 > 0:
			imp += ts[i+1] - t * 2
	print(imp)
