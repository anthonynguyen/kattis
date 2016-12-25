#!/usr/bin/env python3

s = 0
for i in range(int(input())):
	p = input()
	s += int(p[:-1])**int(p[-1])
print(s)
