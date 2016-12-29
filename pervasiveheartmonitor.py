#!/usr/bin/env python3

while True:
	try:
		line = input().split()
	except:
		break

	name = []
	hr = []
	for p in line:
		try:
			hr.append(float(p))
		except:
			name.append(p)
	print(sum(hr) / len(hr), " ".join(name))
