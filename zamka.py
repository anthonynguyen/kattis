#!/usr/bin/env python3

L = int(input())
D = int(input())
X = int(input())

N = D + 1
M = 0
for i in range(L, D + 1):
	s = sum(map(int, str(i)))
	if s != X:
		continue
	if i < N:
		N = i
	M = i
print(N)
print(M)
