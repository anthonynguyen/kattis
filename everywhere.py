#!/usr/bin/env python3

t = int(input())
for _ in range(t):
	n = int(input())
	l = set()
	for _ in range(n):
		l.add(input())
	print(len(l))
