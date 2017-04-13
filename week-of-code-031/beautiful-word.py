"""
hacker rank
week of code 031 day 01
"""


class Word(object):
    def __init__(self, word):
        self.word = list(word)
        self.length = len(self.word)
        self.index = int()
        self.state = True
        self.vowel_set = list('aeiouy')
        self.reason = 'Beautiful Word'
        self.is_beautiful()


    def is_beautiful(self):
        for index, char in enumerate(self.word):
            self.index = index
            if self._continue:
                self._check_next(self.index)


    @property
    def _continue(self):
        if self.length-1 > self.index and self.state is not False:
            return True
        else:
            return False



    def _check_next(self, i):
        if self.word[i] == self.word[i+1]:
            self.state = False
            self.reason = 'Consecutive Characters'
            return
        elif self.word[i] in self.vowel_set:
            self._check_vowels(self.word[i], self.word[i+1])

    def _check_vowels(self, a, b):
        if a in self.vowel_set and b in self.vowel_set:
            self.state = False
            self.reason = 'Consecutive Vowels'
            return


def get_input():
    return raw_input().strip()


def main():
    data = get_input()
    w = Word(data)
    if w.state:
        print 'Yes'
    else:
        print 'No'


if __name__ == '__main__':
    main()

