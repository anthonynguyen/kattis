#!/usr/bin/env python3

def dsum(n):
	return sum(map(int, str(n)))

n = int(input())
while n != 0:
	p = 11
	dsn = dsum(n)
	while dsum(n * p) != dsn:
		p += 1
	print(p)
	n = int(input())
