#!/bin/python

import sys

def get_input():
    n,m = raw_input().strip().split(' ')
    n,m = [int(n),int(m)]
    return n, m


def main():
    p, c = get_input()
    if p/c:
        print p % c
    elif c % p == 0:
        print 0
    else:
        print (p - (c % p))


if __name__ == '__main__':
    main()
