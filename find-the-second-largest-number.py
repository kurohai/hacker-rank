#!/bin/env python

class UniqList(list):
    """docstring for UniqList"""

    def __init__(self, arg):
        super(UniqList, self).__init__()
        self.extend(arg)

    def uniq(self):
        tset = list(set(self))
        self.__init__(tset)


def get_input():
    return int(raw_input()), raw_input()


def parse_input(s):
    return UniqList([int(a) for a in s.split()])


def answer(a):
    if len(a) > 1:
        print a[-2]
    else:
        print a[-1]


def main():
    n, a = get_input()
    array = parse_input(a)
    array.uniq()
    array.sort()
    answer(array)

if __name__ == '__main__':
    main()
