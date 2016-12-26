#!/usr/bin/env python3

penalty = {}
solved = {}
line = input()
while line != "-1":
	m, q, s = line.split()
	m = int(m)
	s = (s == "right")
	if not s and q not in solved:
		if q not in penalty:
			penalty[q] = 20
		else:
			penalty[q] += 20
	elif s:
		solved[q] = m
	line = input()
score = 0
for q in solved:
	score += solved[q]
	if q in penalty:
		score += penalty[q]
print(len(solved), score)
