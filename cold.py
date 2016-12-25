#!/usr/bin/env python3

input()
print(sum([1 if int(j) < 0 else 0 for j in input().split()]))
