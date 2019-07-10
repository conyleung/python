#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math
i = int(input())
wi = []
a = 1
for a in range(1,i+1):
    if a <= i:
        sq = a * a
        wi.append(sq)
        a += 1
    else:
        print(wi)
print(wi)
