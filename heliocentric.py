#!/usr/bin/env python3

E, M = 365, 687
n = 1
while True:
	try:
		e, m = (int(x) for x in input().split())
	except:
		break
	e = (-e) % E
	m = (-m) % M
	for i in range(E*M):
		if i % E == e and i % M == m:
			print("Case {}: {}".format(n, i))
			n += 1
			break
