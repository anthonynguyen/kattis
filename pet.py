#!/usr/bin/env python3

n = -1
m = 0
for i in range(5):
	s = [int(j) for j in input().split()]
	if sum(s) > m:
		m = sum(s)
		n = i
print(n+1, m)
