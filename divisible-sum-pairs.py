#!/bin/python

import sys


def get_input():
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = map(int, raw_input().strip().split(' '))
    if len(a) == n:
        return n, k, a


def make_pairs(arr):
    result = list()
    for i in arr:
        p = [(i, x) for x in arr if i < x]
        print i, p
        result.extend(p)
    return result


def test_pairs(pairs, target):
    result = int()
    for p in pairs:
        a = p[0]
        b = p[1]
        if (a + b) % target == 0:
            print 'pair {0} works with mod: {1}'.format((a,b), ((a + b) % target))
            result += 1
        else:
            print 'pair {0} DOES NOT with mod: {1}'.format((a,b), ((a + b) % target))

    return result


def total_pairs(icount):
    result = int()
    while icount > 0:
        icount -= 1
        result += icount
    return result

def main():
    icount, target, arr = get_input()
    pairs = make_pairs(arr)
    print test_pairs(pairs, target)
    print 'pairs required: ', total_pairs(icount)
    print 'pairs found: ', len(pairs)
    print 'duplicates: {0}'.format(
                                   (len(pairs) - len(set(arr)))
                                   )
    print 'uniques: {0}'.format(
                                   (len(arr) - len(set(arr)))
                                   )


if __name__ == '__main__':
    main()
