#!/usr/bin/env python3

w = "-"
for c in input():
	if w[-1] != c:
		w += c
print(w[1:])
