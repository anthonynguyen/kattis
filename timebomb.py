#!/usr/bin/env python3

numbers = [
	["*****", "*   *", "*****"],
	["     ", "     ", "*****"],
	["*** *", "* * *", "* ***"],
	["* * *", "* * *", "*****"],
	["  ***", "  *  ", "*****"],
	["* ***", "* * *", "*** *"],
	["*****", "* * *", "*** *"],
	["    *", "    *", "*****"],
	["*****", "* * *", "*****"],
	["* ***", "* * *", "*****"]
]
inp = []
while True:
	try:
		inp.append(input())
	except:
		break
sideways = list(zip(*inp[::-1]))
code = 0
for i in range(0, len(sideways), 4):
	try:
		num = ["".join(x) for x in sideways[i:i+3]]
		ii = numbers.index(num)
		code = code * 10 + ii
	except:
		continue

if code % 6:
	print("BOOM!!")
else:
	print("BEER!!")
