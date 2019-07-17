#!/usr/bin/env python
#-*- coding: utf-8 -*-
def jo(x,q):
    s = 0
    if q == 'double':
        for i in range(0,x+1):
            if i % 2 == 0:
                s += i
                continue
        print(s)
    else:
        for i in range(0,x+1):
            if i % 2 != 0:
                s += i
                continue
        print(s)
    return;


if __name__ == '__main__':
    x = int(input('please input a number:'))
    q = input('please input single or double:')
    jo(x,q)

