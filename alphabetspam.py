#!/usr/bin/env python3

s = input()
white = lower = upper = symbo = 0
for c in s:
	if c == "_":
		white += 1
	elif c.isalpha():
		if c.islower():
			lower += 1
		else:
			upper += 1
	else:
		symbo += 1
ss = white + lower + upper + symbo
print(white / ss)
print(lower / ss)
print(upper / ss)
print(symbo / ss)
