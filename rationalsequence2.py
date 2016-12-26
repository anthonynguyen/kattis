#!/usr/bin/env python3

for _ in range(int(input())):
	k, pq = input().split()
	k = int(k)
	p, q = (int(x) for x in pq.split("/"))
	path = ""
	while (p, q) != (1, 1):
		if  p < q:
			path = "L" + path
			q -= p
		else:
			path = "R" + path
			p -= q

	n = 1
	for s in path:
		if s == "L":
			n = n * 2
		else:
			n = n * 2 + 1
	print(k, n)
