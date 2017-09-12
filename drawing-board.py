#!/bin/python

import sys


def make_it_odd(x):
    if x % 2:
        return x
    else:
        return x + 1


def get_page_turns(x):
    return (x - 1) / 2


def get_least_turns(x, y):
    turns_to_page = get_page_turns(x)
    turns_to_end = get_page_turns(y)
    turns_from_end = turns_to_end - turns_to_page
    return min([turns_to_page, turns_from_end])


def solve(n, p):
    n = make_it_odd(n)
    p = make_it_odd(p)
    return get_least_turns(p, n)


def get_input():
    n = int(raw_input().strip())
    p = int(raw_input().strip())
    return n, p


def main():
    n, p = get_input()
    result = solve(n, p)
    print(result)


if __name__ == '__main__':
    main()
