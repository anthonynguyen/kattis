#!/usr/bin/env python3

import re
r, c = (int(x) for x in input().split())
board = []
for _ in range(r):
	board.append(input())

wordre = re.compile(r"\b(\w{2,})\b")
word = "z" * max(r, c)

# find horizontal
for row in board:
	for w in wordre.findall(row):
		if w < word:
			word = w

# transpose and find horizontal again (vertical)
board = zip(*board)
for col in board:
	for w in wordre.findall("".join(col)):
		if w < word:
			word = w

print(word)
