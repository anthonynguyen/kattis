#!/usr/bin/env python3

for _ in range(int(input())):
	name, postsecondary, dob, courses = input().split()
	psyear = int(postsecondary[:4])
	dobyear = int(dob[:4])
	courses = int(courses)
	if psyear >= 2010 or dobyear >= 1991:
		print(name, "eligible")
	elif courses >= 41:
		print(name, "ineligible")
	else:
		print(name, "coach petitions")
