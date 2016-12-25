#!/usr/bin/env python3

import math

p = input().split()
h, v = int(p[0]), int(p[1])
print(math.ceil(h / math.sin(math.radians(v))))
