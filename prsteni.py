#!/usr/bin/env python3

from fractions import gcd
input()
def reduce(a, b):
	return (a // gcd(a, b), b // gcd(a, b))
n, d = 1, 1
r = [int(x) for x in input().split()]
for i in range(1, len(r)):
	n, d = reduce(n * r[i-1], d * r[i])
	print("{}/{}".format(n, d))
