#!/bin/bash




def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def main():
    A = [random() for i in xrange(10**4)]
    B = [random() for i in xrange(10**4)]
    print A
    print gcd(8, 9)

if __name__ == '__main__':
    main()
