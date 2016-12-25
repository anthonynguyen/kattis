#!/usr/bin/env python3

dim = [int(x) for x in input().split()]
dim.sort()
print(dim[0] * dim[2])
