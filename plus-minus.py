#!/bin/python

from decimal import Decimal, getcontext


def get_input():
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    return n, arr


def get_values(arr):
    result = dict()
    result['p'] = int()
    result['n'] = int()
    result['z'] = int()
    for a in arr:
        result[check_pos_neg(a)] += 1
    return result


def check_pos_neg(n):
    if n > 0:
        return 'p'
    if n < 0:
        return 'n'
    if n == 0:
        return 'z'


def do_math(vals, count):
    getcontext().prec = 6
    p = Decimal((vals['p']) / float(count))
    n = Decimal((vals['n']) / float(count))
    z = Decimal((vals['z']) / float(count))
    return (p, n, z)


def output(results):
    for r in results:
        print '{0:.6f}'.format(round(r, 6))


def main():
    count, arr = get_input()
    vals = get_values(arr)
    results = do_math(vals, count)
    output(results)


if __name__ == '__main__':
    main()
