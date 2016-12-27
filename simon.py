#!/usr/bin/env python3

for _ in range(int(input())):
	c = input()
	if c[:10] == "simon says":
		print(c[11:])
