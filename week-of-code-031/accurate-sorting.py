"""
hacker rank
week of code 031 day 02
"""


"""not complete"""

class Sorterator(object):
    def __init__(self, query):
        self.query = query
        self.sortable = 'Unknown'
        self.index = int()

    def sort(self):
        for i, n in enumerate(query):
            self.index = i
            if query[i+1] < n:
                pass

    def __repr__(self):
        return str(self.sortable)


def get_input():
    q = int(raw_input().strip())

    queries = list()
    for a0 in xrange(q):
        n = int(raw_input().strip())
        queries.append(map(int, raw_input().strip().split(' ')))
    return queries


def main():
    data = get_input()
    for query in data:
        print Sorterator(query)


if __name__ == '__main__':
    main()

