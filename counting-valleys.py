#!/usr/bin/env python2


class HikeTracker(object):
    """docstring for HikeTracker"""

    def __init__(self, sequence):
        super(HikeTracker, self).__init__()
        self.sequence = [c for c in sequence]
        self.valley_count = int()
        self.current_elevation = int()
        self._do_hike()

    def _do_hike(self):
        for step in self.sequence:
            self._do_step(step)

    def _do_step(self, step):
        if step == 'U':
            self._step_up()
        else:
            self._step_down()

    def _step_up(self):
        if self.current_elevation == -1:
            self.valley_count += 1
        self.current_elevation += 1

    def _step_down(self):
        self.current_elevation -= 1


def get_input():
    steps = raw_input().strip()
    sequence = raw_input().strip()
    return steps, sequence


def main():
    steps, sequence = get_input()
    hike = HikeTracker(sequence)
    print(hike.valley_count)


if __name__ == '__main__':
    main()
