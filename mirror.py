#!/usr/bin/env python3

for i in range(int(input())):
	r, c = (int(x) for x in input().split())
	m = []
	for rr in range(r):
		m.append(input())
	print("Test", i + 1)
	for rr in m[::-1]:
		print(rr[::-1])
