#!/usr/bin/env python3

gun = [int(x) for x in input().split()]
emm = [int(x) for x in input().split()]

g = sum(range(gun[0], gun[1] + 1)) / (gun[1] - gun[0] + 1)
g += sum(range(gun[2], gun[3] + 1)) / (gun[3] - gun[2] + 1)

e = sum(range(emm[0], emm[1] + 1)) / (emm[1] - emm[0] + 1)
e += sum(range(emm[2], emm[3] + 1)) / (emm[3] - emm[2] + 1)

if g > e:
	print("Gunnar")
elif g < e:
	print("Emma")
else:
	print("Tie")
