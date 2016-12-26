#!/usr/bin/env python3

line = input()
while True:
	p = line.split()
	t1 = [int(x) for x in p[-2].split(":")]
	t2 = [int(x) for x in p[-1].split(":")]
	hd = t2[0] - t1[0]
	md = t2[1] - t1[1]
	if md < 0:
		hd -= 1
		md += 60
	print(" ".join(p[:-2]), hd, "hours", md, "minutes")

	try:
		line = input()
	except:
		break
