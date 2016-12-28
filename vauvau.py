#!/usr/bin/env python3

a, b, c, d = (int(x) for x in input().split())
men = [int(x) for x in input().split()]
for man in men:
	dog = 0
	if 0 < man % (a + b) <= a:
		dog	 += 1
	if 0 < man % (c + d) <= c:
		dog	 += 1
	print(["none", "one", "both"][dog])
