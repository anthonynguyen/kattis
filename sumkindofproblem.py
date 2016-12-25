#!/usr/bin/env python3

for _ in range(int(input())):
	k, n = (int(x) for x in input().split())
	s1 = n * (n + 1) // 2
	s2 = n * n
	s3 = s1 * 2
	print(k, s1, s2, s3)
