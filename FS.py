#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math
import os
fs = [1,1]
n = int(input("please input a number:"))
if n <=2:
    print(fs)
    os.sys.exit()
else:
    for i in range(2,n+1):
        a = fs[i-1]+fs[i-2]
        fs.append(a)
print(fs)
