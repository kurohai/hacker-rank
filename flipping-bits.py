#!/bin/python


def get_input():
    uints = list()
    for i in xrange(int(raw_input().strip())):
        uints.append(int(raw_input().strip()))
    return uints


def main():
    uints = get_input()
    for i in uints:
        print 4294967295 - i


if __name__ == '__main__':
    main()
