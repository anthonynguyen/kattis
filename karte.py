#!/usr/bin/env python3

deck = {
	"P": {},
	"K": {},
	"H": {},
	"T": {},
}

inp = input()
cards = [inp[i:i+3] for i in range(0, len(inp), 3)]
greska = False
for c in cards:
	if c[1:] in deck[c[0]]:
		greska = True
		print("GRESKA")
		break

	deck[c[0]][c[1:]] = 1

if not greska:
	print(" ".join([str(13 - len(deck[suit]))	 for suit in "PKHT"]))
