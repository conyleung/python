#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def ra(x = 7):
    import random
    return random.randint(1, x)


if __name__ == '__main__':
    print(ra())
