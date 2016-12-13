

def char_gen(n):
    """do the char thing"""
    i = 0
    chars = 'abcdefghijklmnopqrstuvwxyz'
    while i < n:
        i += 1
        yield chars[i-1]


def line_gen(i):
    """do the line thing"""
    line = str()
    gen = char_gen(i)
    char = next(gen, None)
    line = char
    while char is not None:
        char = next(gen, None)
        if char is None:
            return line
        line = '{c}-{L}-{c}'.format(
            c=char,
            L=line,
        )
    return line


def main(n):
    """do the main thing"""
    i = n
    lines = list()
    while i > 0:
        lines.append(line_gen(i))
        i -= 1
    c = n * 2 - 1
    while c > 0:
        if c >= n:
            line = '{0}'.format(lines[c-n])
        else:
            l = [x for x in reversed(lines)]
            line = '{0}'.format(l[c-1])
            # print l[c-n]

        while len(line) < ((n + (n - 1)) * 2) - 1:
            line = '-' + line + '-'
        print line

        c -= 1


if __name__ == '__main__':
    # n = raw_input()
    n = 10
    main(n)
