#!/usr/bin/env python3

morse = {
	"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
	"F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
	"K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
	"P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
	"U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
	"Z": "--..", "_": "..--", ",": ".-.-", ".": "---.", "?": "----"
}
reverse = {morse[c]: c for c in morse}

line = input()
while True:
	m = ""
	length = []
	for c in line:
		cm = morse[c]
		length.append(len(cm))
		m += cm
	i = 0
	o = ""
	for l in length[::-1]:
		o += reverse[m[i:i+l]]
		i += l
	print(o)
	try:
		line = input()
	except:
		break
