#!/usr/bin/env python3

line = input()
while line != "0":
	n = int(line)
	figure = []
	m = 0
	for _ in range(n):
		ll = input()
		m = max(m, len(ll))
		figure.append(ll)
	for i, l in enumerate(figure):
		ll = len(l)
		figure[i] = l + " " * (m - ll)
	flip = zip(*figure[::-1])
	for l in flip:
		ll = "".join(l).replace("-", ")").replace("|", "-").replace(")", "|").rstrip()
		if ll:
			print(ll)
	line = input()
	if line != "0":
		print()
