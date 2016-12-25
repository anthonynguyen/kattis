#!/usr/bin/env python3

n = int(input())
s = 1
while n != 0:
	names = []
	for _ in range(n):
		names.append(input())
	e = []
	o = []
	for i, n in enumerate(names):
		if i % 2:
			o.insert(0, n)
		else:
			e.append(n)
	print("SET", s)
	for n in e + o:
		print(n)
	s += 1
	n = int(input())
