#!/usr/bin/env python3

for _ in range(int(input())):
	mess = input()
	k = 1
	while k * k < len(mess):
		k += 1
	mess += "*" * (k * k - len(mess))
	sq = []
	sq = [mess[i:i+k] for i in range(0, len(mess), k)]
	for i in range(k):
		for j in range(k)[::-1]:
			if sq[j][i] != "*":
				print(sq[j][i], end = "")
	print()
