import sys
import pickle
from itertools import combinations, permutations


def p_mul(x, y):
    return tuple([x[yy - 1] for yy in y])


def p_inv(x):
    return tuple([x.index(i + 1) + 1 for i in range(len(x))])


def p_rev(p, x, y):
    if x == 0:
        return p[y::-1] + p[y+1:]
    if y == len(p) - 1:
        return p[:x] + p[:x-1:-1]
    return p[:x] + p[y:x-1:-1] + p[y+1:]


def p_bp(p):
    """Array of breakpoints indexed between i, i+1."""
    b = (0,) + p + (len(p) + 1,)
    bp = []
    for i in range(len(b) - 1):
        if abs(b[i+1] - b[i]) != 1:
            bp.append(i)
    return bp


def n_table(n):
    i = tuple(range(1, n+1))
    table = {i: 0}
    ring = set([i])
    new_ring = set()
    perms = set([x for x in permutations(range(1, n+1))])
    n_fac = len(perms)
    while len(table) < n_fac:
        for p in ring:
            dep = table[p]
            for i, j in combinations(range(n), 2):
                pr = p_rev(p, i, j)
                if not pr in table:
                    new_ring.add(pr)
                    table[pr] = dep + 1
        ring, new_ring = new_ring, set()
    perms = perms - set(table.keys())
    new_perms = perms.copy()
    # Search from permutation to table entry - unused
    while len(table) < n_fac:
        for p in perms:
            if p in table:
                continue
            best_dist = float('inf')
            for i, j in combinations(range(n), 2):
                pr = p_rev(p, i, j)
                if pr in table and table[pr] + 1 < best_dist:
                    best_dist = table[pr] + 1
            if best_dist < float('inf'):
                table[p] = best_dist
                new_perms.remove(p)
        perms = new_perms
    return table


if __name__ == '__main__':
    pairs = ['3 9 10 4 1 8 6 7 5 2','2 9 8 5 1 7 3 4 6 10']
    pi = p_mul(p_inv(pairs[1]), pairs[0])
    sys.stdout.write('\n')