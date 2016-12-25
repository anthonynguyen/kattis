#!/usr/bin/env python3

a, b, c = (int(x) for x in input().split())

# lol
if a + b == c:
	print("{}+{}={}".format(a, b, c))
elif a == b + c:
	print("{}={}+{}".format(a, b, c))
elif a - b == c:
	print("{}-{}={}".format(a, b, c))
elif a == b - c:
	print("{}={}-{}".format(a, b, c))
elif a / b == c:
	print("{}/{}={}".format(a, b, c))
elif a == b / c:
	print("{}={}/{}".format(a, b, c))
elif a * b == c:
	print("{}*{}={}".format(a, b, c))
elif a == b * c:
	print("{}={}*{}".format(a, b, c))
