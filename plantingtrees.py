#!/usr/bin/env python3

n = int(input())
tr = sorted([int(x) for x in input().split()], reverse = True)
earliest = n + 2
for i, t in enumerate(tr):
	if i + 2 + t > earliest:
		earliest = i + 2 + t
print(earliest)
