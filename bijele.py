#!/usr/bin/env python3

i = input().split()
t = [1, 1, 2, 2, 2, 8]
o = [str(t[j] - int(p)) for j, p in enumerate(i)]
print(" ".join(o))
