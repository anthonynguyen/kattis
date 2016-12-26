#!/usr/bin/env python3

board = []
for i in range(7):
	board.append(input())

m = 0
for y, r in enumerate(board):
	for x, c in enumerate(r):
		if c != "o":
			continue

		# left
		if x > 1:
			if board[y][x-1] == "o" and board[y][x-2] == ".":
				m += 1

		# right
		if x < 5:
			if board[y][x+1] == "o" and board[y][x+2] == ".":
				m += 1

		# up
		if y > 1:
			if board[y-1][x] == "o" and board[y-2][x] == ".":
				m += 1

		# down
		if y < 5:
			if board[y+1][x] == "o" and board[y+2][x] == ".":
				m += 1
print(m)
