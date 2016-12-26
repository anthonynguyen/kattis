#!/usr/bin/env python3

import itertools
num = int(input())
points = []

# distance from a to b
def d(a, b):
	global points
	return round(((points[a][0] - points[b][0])**2 + (points[a][1] - points[b][1])**2)**0.5)

# read all points in
for _ in range(num):
	points.append([float(x) for x in input().split()])

# precompute distance matrix
dists = [[0 for i in range(num)] for j in range(num)]
for i in range(num):
	for j in range(i + 1, num):
		dd = d(i, j)
		dists[i][j] = dd
		dists[j][i] = dd

# try all permutations (hopefully this is fast enough)
# lol, this is not fast enough, see tsp.cpp for a faster solution in C++
minp = []
mind = -1
for p in itertools.permutations(range(1, len(points))):
	pp = [0] + list(p)
	dist = sum([dists[n][pp[i+1]] for i, n in enumerate(pp[:-1])])
	if mind == -1 or dist < mind:
		minp = pp
		mind = dist
for t in minp:
	print(t)
