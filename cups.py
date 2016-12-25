#!/usr/bin/env python3

n = int(input())
c = []

for i in range(n):
	cupp = input().split()
	try:
		cup = (int(cupp[0]) / 2, cupp[1])
	except:
		cup = (int(cupp[1]), cupp[0])

	c.append(cup)

c.sort()
for cc in c:
	print(cc[1])
