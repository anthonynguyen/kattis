#!/usr/bin/env python3

while True:
	try:
		a, op, b = input().split()
	except:
		break
	a, b = int(a), int(b)
	if op == "+":
		answer = a + b
	elif op == "*":
		answer = (a % 10000) * (b % 10000)
	else:
		a %= 10000
		answer = 1
		while b > 0:
			if b % 2:
				answer = (answer * a) % 10000
				b -= 1
			a = (a * a) % 10000
			b //= 2
	print(answer % 10000)
