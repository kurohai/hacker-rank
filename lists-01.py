
input1 = '5'
input2 = '2 3 6 6 5'


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
    return s.split()

def main():
    n, a = get_input_test()
    array = parse_input(a)
    array = uniq(sort(array))
    print array[-2]

if __name__ == '__main__':
    main()
