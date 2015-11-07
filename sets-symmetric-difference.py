
def main(m2, n2):
    a = set([i for i in m2.difference(n2)])
    a.update([i for i in n2.difference(m2)])
    b = [i for i in a]
    b.sort()
    print '\n'.join(str(i) for i in b)




if __name__ == '__main__':
    m1 = int(raw_input())
    m2 = set([i for i in map(int, raw_input().split(' '))])
    n1 = int(raw_input())
    n2 = set([i for i in map(int, raw_input().split(' '))])
    main(m2, n2)
