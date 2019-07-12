#!/usr/bin/env python
#!-*- coding: utf-8 -*-
import math
year = int(input('please input a number:'))
ff = year % 4
fff = year % 400
if ff == 0:
    if fff == 0:
        print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    if fff == 0:
        print("This is a leap year")
    else:
        print("This is not a leap year")
