#!/bin/python


def get_input():
    target = raw_input().strip()
    count = int(raw_input().strip())
    array = raw_input().strip().split()
    return count, target, array


def main():
    c, t, a = get_input()
    for i in xrange(c):
        if int(a[i]) is int(t):
            print i


if __name__ == '__main__':
    main()
