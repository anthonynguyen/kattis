#!/usr/bin/env python3

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
line = input()
while line != "0":
	p = line.split()
	message = [abc[(abc.index(c) + int(p[0])) % len(abc)] for c in p[1]]
	print("".join(message[::-1]))
	line = input()
