#!/usr/bin/env python3

for _ in range(int(input())):
	a = input()
	b = input()
	d = ["." if a[i] == b[i] else "*" for i, c in enumerate(a)]
	print(a)
	print(b)
	print("".join(d))
	print()
