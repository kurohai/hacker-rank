#!/bin/env python


# problem approach
# status is the current terrain; mountain or valley.
# height is current elevation relative to sea level.
# terrain count is incremented when terrain begins.
# status is updated when terrain begins


# step > _step_up or _step_down
# if height before step is 0, update status
# if height before step is -1 AND step direction is up, update status
# if height before step is 1 and step direction is down, update status


class Hike(dict):
    def __init__(self):
        self.height = 0
        self.on_mountain = False
        self.mountain_count = 0
        self.in_valley = False
        self.valley_count = 0

    def step(self, direction):
        if direction.lower() == 'u':
            self._step_up()
        elif direction.lower() == 'd':
            self._step_down()

    def _step_up(self):
        if self.height == 0:
            self.on_mountain = True
            self.mountain_count += 1
        elif self.height == int(-1):
            self.in_valley = False
        self.height += 1

    def _step_down(self):
        if self.height == 0:
            self.in_valley = True
            self.valley_count += 1
        elif self.height == 1:
            self.on_mountain = False
        self.height -= 1

    def status(self):
        print self.height
        if self.on_mountain:
            print 'mountian'
        elif self.in_valley:
            print 'valley'
        else:
            print 'sea level'


def get_input():
    a = int(raw_input().strip())
    b = raw_input().strip()
    return a, b


def main():
    step_count, steps = get_input()
    hike = Hike()
    for step in steps:
        hike.step(step)
    print hike.valley_count


if __name__ == '__main__':
    main()
