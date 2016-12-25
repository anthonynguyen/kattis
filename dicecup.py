#!/usr/bin/env python3

d = input().split()
n = int(d[0])
m = int(d[1])
sumd = {}
for i in range(1, n + 1):
	for j in range(1, m + 1):
		if i + j in sumd:
			sumd[i + j] += 1
		else:
			sumd[i + j] = 0

sums = [(sumd[i], i) for i in sumd]
sums.sort()

m = sums[-1][0]
for i in sums:
	if i[0] == m:
		print(i[1])
