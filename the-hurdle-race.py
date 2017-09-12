#!/bin/python


def get_input():
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    height = map(int, raw_input().strip().split(' '))

    return [n, k, height]


def main():
    n, k, height = get_input()
    mheight = max(height)
    if k >= mheight:
        return 0
    else:
        return mheight - k


if __name__ == '__main__':
    print main()
