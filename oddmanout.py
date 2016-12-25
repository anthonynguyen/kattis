#!/usr/bin/env python3

for n in range(int(input())):
	g = int(input())
	c = input().split()
	for i in c:
		if c.count(i) == 1:
			print("Case #{}: {}".format(n + 1, i))
			break
