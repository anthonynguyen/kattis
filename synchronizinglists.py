#!/usr/bin/env python3

n = int(input())
while n != 0:
	l1 = []
	l2 = []
	for _ in range(n):
		l1.append(int(input()))
	for _ in range(n):
		l2.append(int(input()))
	l1_s = sorted(l1)
	l2_s = sorted(l2)
	corresp = [l2_s[l1_s.index(i)] for i in l1]
	for x in corresp:
		print(x)
	n = int(input())
	if n != 0:
		print()
