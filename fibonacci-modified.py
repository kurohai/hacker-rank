#!/bin/python


def get_input():
    t1, t2, n = raw_input().strip().split(' ')
    n, t1, t2 = [long(n), int(t1), int(t2)]
    return n, t1, t2


def do_math(n, t1, t2):
    for i in xrange(n-2):
        tmp = t2
        t2 = t1 + (t2**2)
        t1 = tmp
    return t2


def main():
    n, t1, t2 = get_input()
    print do_math(n, t1, t2)


if __name__ == '__main__':
    main()
