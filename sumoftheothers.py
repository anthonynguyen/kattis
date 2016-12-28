#!/usr/bin/env python3

while True:
	try:
		nums = [int(x) for x in input().split()]
	except:
		break
	for i, n in enumerate(nums):
		if n == sum(nums[:i] + nums[i+1:]):
			print(n)
			break
