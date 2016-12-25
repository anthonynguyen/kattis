#!/usr/bin/env python3

n = int(input())

for i in range(n):
	x = int(input())
	print("{} is {}".format(x, "odd" if x % 2 else "even"))
