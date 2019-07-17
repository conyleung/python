#!/usr/bin/env python
#-*- coding: utf-8 -*-
def tri(n):
    for i in range(0,n+1):
        star = (2*i+1)*'*'
        space = (n-i)*'  '
        s = space + star# + space
        print(s)

if __name__ == '__main__':
    n = int(input("please input a number:"))
    tri(n)
