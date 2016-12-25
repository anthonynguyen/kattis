#!/usr/bin/env python3

sentence = input().split()
out = []

for word in sentence:
	w = ""
	i = 0
	while i < len(word):
		if i < len(word) - 2:
			if word[i] in "aeiou" and word[i+1] == "p" and word[i+2] == word[i]:
				w += word[i]
				i += 3
				continue
		w += word[i]
		i += 1
	out.append(w)
print(" ".join(out))
