#!/usr/bin/env python
#-*- coding: utf-8 -*-
import math
def prime():
    num = int(input("please input a number:"))
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            print("This is not a prime")
            break
    else:
        print("This is a prime")
def main():
    print(prime())
if __name__ == '__main__':
    main()

