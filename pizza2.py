#!/usr/bin/env python3

import math
r, c = (int(x) for x in input().split())
print("{0:.6f}".format(((r-c)**2*math.pi) / (r*r*math.pi) * 100))
