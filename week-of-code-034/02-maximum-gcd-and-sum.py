#!/bin/bash

from pprint import pprint
import random

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def main():
    A = [random.randint(1, (10**6)*5) for i in xrange(10**6)]
    B = [random.randint(1, (10**6)*5) for i in xrange(10**6)]
    c = set()
    # c = list()
    for i in xrange(10**6):
        gdmflan = gcd(A[i], B[i])
        c.update([gdmflan])
    # for i in xrange(10**6):
    #     gdmflan = gcd(A[i], B[i])
    #     if not gdmflan in c:
    #         c.append(gdmflan)
    # d = set(c)
    # pprint(d)
    for i in xrange(100):
        if not i in c:
            print i

    # print gcd(8, 9)

if __name__ == '__main__':
    main()
