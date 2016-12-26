#!/usr/bin/env python3

lines = []
line = input()
while True:
	lines.append(line)
	try:
		line = input()
	except:
		break

n = max([len(line) for line in lines])
penalty = []
for line in lines[:-1]:
	penalty.append((n - len(line)) ** 2)
print(sum(penalty))
