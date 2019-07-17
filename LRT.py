#!/usr/bin/env python
#-*- coding: utf-8 -*-
def lrt(n,y):
    star = ''
    space = ' '
    s = []
    for i in range(0,n+1):
        star += '*'
        space = (n-i)*' '
        if y == 'left':
            s = star + space
        elif y == 'right':
            s = space + star
        print(s)

if __name__ == '__main__':
    n = int(input("please input a number:"))
    y = input("please input left or right:")
    lrt(n,y)

