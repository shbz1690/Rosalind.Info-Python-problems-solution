def pdist(s1, s2):
    size = min(len(s1), len(s2))
    diffs = 0
    for i in range(0, size):
        if s1[i] != s2[i]:
            diffs += 1
    return float(diffs) / float(size)


if __name__ == "__main__":
    lines = list(open("input.dat"))
    N = len(lines)
    lines = map(lambda x: x.rstrip(), lines)
    assert N % 2 == 0
    strings = []
    buf = ""
    for i in range(1, len(lines)):
        if lines[i][0] == '>':
            strings.append(buf)
            buf = ""
        else:
            buf += lines[i]
    strings.append(buf)

    for i in range(0, len(strings)):
        for j in range(0, len(strings)):
            print pdist(strings[i], strings[j]),
        print ""