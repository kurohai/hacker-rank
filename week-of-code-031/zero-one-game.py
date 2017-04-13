"""
hacker rank
week of code 031 day 03
"""


def get_input():
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n = int(raw_input().strip())
        yield map(int, raw_input().strip().split(' '))


class DamnThing(object):
    """docstring for DamnThing"""
    def __init__(self, game):
        super(DamnThing, self).__init__()
        self.zero = int()
        self.move = int()
        self.game = game
        self.index = int(0)
        self.done = False

    @property
    def length(self):
        return len(self.game)

    @property
    def _current_bit(self):
        return self.game[self.index]

    @property
    def _next_bit(self):
        return self.game[self.index+1]

    @property
    def _last_bit(self):
        return self.game[-1]

    @property
    def winner(self):
        if self.done:
            if self.move % 2:
                return 'Alice'
            else:
                return 'Bob'
        else:
            return 'Thing needs more do'

    @property
    def cont(self):
        if self.index+1 < self.length:
            return True
        elif self.index+1 == self.length and self._current_bit == 0:
            return True

    def tripz(self):
        if self.zero == 3:
            self.move += 1
            self.zero -= 1

    def check_one(self):
        if self._next_bit == 0:
            self.move += 1
        else:
            self.zero = 0

    def do(self):
        while self.cont:
            if self._current_bit == 0:
                self.zero += 1
                self.tripz()
            elif self._current_bit == 1 and self.zero >= 1:
                self.check_one()
            self.index += 1

        self.done = True


def main():
    userinput = get_input()
    nextin = userinput.next()
    go = True
    zero = 0
    move = 0
    while go:
        damnthing = DamnThing(nextin)
        damnthing.do()
        print damnthing.winner

        try:
            nextin = userinput.next()
        except StopIteration:
            go = False


if __name__ == '__main__':
    main()
