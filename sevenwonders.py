#!/usr/bin/env python3

cards = input()
T = cards.count("T")
G = cards.count("G")
C = cards.count("C")
bonus = min(T, G, C) * 7
print(T*T + G*G + C*C + bonus)
