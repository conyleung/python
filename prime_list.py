#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math
a = int(input('please input a number:'))
pr = [x for x in range(0,a+1)]
impr = []
if a < 2:
    print([])
for i in pr:
    for k in range(2,int(math.sqrt(i))+1):
        if i % k == 0:
            impr.append(i)
            break
for i in impr:
    pr.remove(i)
    print(pr)

