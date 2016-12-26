#!/usr/bin/env python3

names = []
for _ in range(int(input())):
	names.append(input())

if sorted(names) == names:
	print("INCREASING")
elif sorted(names, reverse = True) == names:
	print("DECREASING")
else:
	print("NEITHER")
