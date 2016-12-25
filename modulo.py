#!/usr/bin/env python3

c = set()
for i in range(10):
	c.add(int(input()) % 42)
print(len(c))
