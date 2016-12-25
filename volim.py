#!/usr/bin/env python3

K = int(input())
N = int(input())

answers = []
for _ in range(N):
	p = input().split()
	answers.append((p[1], int(p[0])))

m = 210
t = 0
for a in answers:
	if m > t and m < t + a[1]:
		if not K % 8:
			print(8)
		else:
			print(K % 8)
		break
	else:
		if a[0] == "T":
			K += 1
	t += a[1]
