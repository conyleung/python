#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math
import random
for x in range(0,21):
    for y in range(0,34):
        for z in range(0,100):
            if 5*x + 3*y + 1/3*z == 100 and x + y + z == 100:
                    print('x=',x,'y=',y,'z=',z)
