#!/bin/python


def get_int():
    return int(raw_input().strip())

def get_input():
    n = get_int()
    gears = list()
    while n > 0:
        n -= 1
        gears.append(get_int())
    return gears


def main():
    gears = get_input()
    for i in gears:
        if i % 2:
            print 'No'
        else:
            print 'Yes'


if __name__ == '__main__':
    main()
