#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math
a = int(input('please input a number:'))
pr = []
for i in range(0,a+1):
    for range(1,int(math.sqrt(i))+1):
        if i % k == 0:
            continue
        else:
            pr.append(i)
print(pr)

