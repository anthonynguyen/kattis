#!/usr/bin/env python3

values = {
	"A": [11, 11],
	"K": [4, 4],
	"Q": [3, 3],
	"J": [20, 2],
	"T": [10, 10],
	"9": [14, 0],
	"8": [0, 0],
	"7": [0, 0]
}

p = input().split()
n = int(p[0])
dom = p[1]
total = 0
for _ in range(n * 4):
	card = input()
	if card[-1] == dom:
		total += values[card[0]][0]
	else:
		total += values[card[0]][1]
print(total)
