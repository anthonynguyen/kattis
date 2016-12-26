#!/usr/bin/env python3

a, b, c = (int(x) for x in input().split())
times = [0 for i in range(100)]
for _ in range(3):
	t = [int(x) for x in input().split()]
	for i in range(t[0], t[1]):
		times[i] += 1
		
cost = 0
for t in times:
	if t == 1:
		cost += t * a
	elif t == 2:
		cost += t * b
	elif t == 3:
		cost += t * c
print(cost)
