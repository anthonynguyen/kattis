#!/usr/bin/env python3

letters = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

for c in range(int(input())):
	last = -1
	out = ""
	for letter in input():
		for i, l in enumerate(letters):
			if letter in l:
				if i == last:
					out += " "
				out += str(i) * (l.index(letter) + 1)
				last = i
	print("Case #{}: {}".format(c + 1, out))
