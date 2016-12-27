#!/usr/bin/env python3

line = input()
while line != "0":
	w, h = 0, 0
	cw, ch = 0, 0
	m = int(line)
	rect = input()
	while rect != "-1 -1":
		rw, rh = (int(x) for x in rect.split())
		if cw + rw > m:
			w = max(w, cw)
			h += ch
			cw = rw
			ch = rh
		else:
			ch = max(ch, rh)
			cw += rw
		rect = input()
	h += ch
	w = max(w, cw)
	print(w, "x", h)
	line = input()
