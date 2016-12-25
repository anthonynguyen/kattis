#!/usr/bin/env python3

adrian = "ABC"
bruno = "BABC"
goran = "CCAABB"

input()
correct = input()
a, b, g = 0, 0, 0
for i, c in enumerate(correct):
	if adrian[i % len(adrian)] == c:
		a += 1
	if bruno[i % len(bruno)] == c:
		b += 1
	if goran[i % len(goran)] == c:
		g += 1
m = max(a, b, g)
print(m)
if a == m:
	print("Adrian")
if b == m:
	print("Bruno")
if g == m:
	print("Goran")
