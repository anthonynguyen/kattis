#!/usr/bin/env python3

x, y, n = (int(i) for i in input().split())
for i in range(1, n + 1):
	if not i % x and not i % y:
		print("FizzBuzz")
	elif not i % x:
		print("Fizz")
	elif not i % y:
		print("Buzz")
	else:
		print(i)
