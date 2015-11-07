


def main(n):
    d = [int(i) for i in raw_input().split(' ')]
    print hash(tuple(d))


if __name__ == '__main__':
    n = int(raw_input())
    main(n-1)
