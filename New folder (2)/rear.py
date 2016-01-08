
def handle_pair(pair):
    lines = pair.split("\n")
    lines = [map(int, l.split()) for l in lines]
    return lines


def inverse_permutation(a):
    p = [None] * len(a)
    for i, n in enumerate(a):
        p[n - 1] = i + 1 
    return p


def apply_permutation(p, b):
    t = []
    for n in b:
        t.append(p[n - 1])
    return t


def reversal_distance(a, b):
    p = inverse_permutation(b)
    a = apply_permutation(p, a)
    l = len(a)
    r = 0

    print '-' * 24

    for j in range(l, 1, -1):
        for i in range(l):
            if a[i] == j:
                break
        if (j - i) > 1:
            print ' '.join([str(0 if x == 10 else x) for x in a]), ':', j
            print ' '.join(([' '] * i) + (['-'] * (j - i)))
            a[i:j] = reversed(a[i:j])
            r += 1

    print r
    
def result(s):
    pairs = s.strip().split("\n\n")
    pairs = [handle_pair(p) for p in pairs]

    for a, b in pairs:
        reversal_distance(a, b)


if __name__ == "__main__":

    small_dataset = """
                   9 6 3 8 10 1 5 2 7 4
3 9 10 6 5 8 7 1 4 2
                    """
    # large_dataset = open('datasets/rosalind_rear.txt').read().strip()

    result(small_dataset)