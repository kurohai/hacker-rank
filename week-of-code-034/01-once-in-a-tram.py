#!/bin/python


def onceInATram(x):
    x += 1
    xs = str(x).zfill(6)
    xxx = xs[:3]
    yyy = xs[3:]
    yyz = xs[3:-1] + '0'
    yzz = xs[3:-2] + '00'
    if sum_str(xxx) == sum_str(yyy):
        return int(str(xxx) + str(yyy))
    elif sum_str(xxx) < sum_str(yzz):
        xxx = do_rollover_thing(xxx)
    elif sum_str(xxx) < sum_str(yyz):
        xxx = do_rollover_thing(xxx)
    return do_iteration(xxx, yyy)


def do_rollover_thing(xxx):
    return str(int(xxx) + 1).zfill(3)


def do_iteration(xxx, yyy):
    while sum_str(xxx) != sum_str(yyy):
        yyy = str(int(yyy) + 1).zfill(3)
        if yyy == '1000':
            yyy = '000'
            xxx = str(int(xxx) + 1).zfill(3)
    return xxx + yyy


def sum_str(n):
    return int(n[0]) + int(n[1]) + int(n[2])


if __name__ == "__main__":
    x = int(raw_input().strip())
    result = onceInATram(x)
    print result
