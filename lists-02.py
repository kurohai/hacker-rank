
input1 = '5'
input2 = '-7 -7 -7 -7 -6'


class UniqList(list):
    """docstring for UniqList"""

    def __init__(self, arg):
        super(UniqList, self).__init__()
        self.extend(arg)

    def uniq(self):
        tset = list(set(self))
        self.__init__(tset)

    def sort2(self):
        tmp1 = list()
        tmp2 = list()
        for i in self.__iter__():
            if i < 0:
                tmp1.append(i)
            else:
                tmp2.append(i)
        tmp1.reverse()
        print 'tmp1: ', tmp1
        print 'tmp2: ', tmp2




def get_input():
    return int(raw_input()), raw_input()


def get_input_test():
    return int(input1), input2


def uniq(n):
    return list(set(n))


def sort(n):
    n.sort()
    return n


def parse_input(s):
    return UniqList([int(a) for a in s.split()])


def answer(a):
    if len(a) > 1:
        print a[-2]
    else:
        print a[-1]

def main():
    n, a = get_input_test()
    array = parse_input(a)
    array.uniq()
    array.sort()
    array.sort2()

    answer(array)


if __name__ == '__main__':
    main()
