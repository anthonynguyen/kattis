#!/usr/bin/env python3

alph = {
	"a": "@","b": "8", "c": "(", "d": "|)", "e": "3",
	"f": "#", "g": "6", "h": "[-]", "i": "|", "j": "_|",
	"k": "|<", "l": "1", "m": "[]\/[]", "n": "[]\[]", "o": "0",
	"p": "|D", "q": "(,)", "r": "|Z", "s": "$", "t": "']['",
	"u": "|_|", "v": "\/", "w": "\/\/", "x": "}{", "y": "`/",
	"z": "2"
}

print("".join([alph[x.lower()] if x.lower() in alph else x for x in input()]))