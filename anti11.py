#!/usr/bin/env python3

# this problem reduces to finding the (n + 2)th Fibonacci number
for _ in range(int(input())):
	n = int(input())
	a, b = 1, 1
	for i in range(n):
		a, b = b, a + b
	print(b % (1000000007))
