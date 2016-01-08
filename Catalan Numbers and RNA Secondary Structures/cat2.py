seq = "AUAU"
seqs = {}
n=len(seq)
pair=['AU', 'UA', 'CG', 'GC']
def cata(sq):
    n=len(sq)
    if n == 0:
        return 1
    if n == 2:
        if sq in pair:
            return 1
        else:
            return 0
    result = 0
    for i in range(1, n):
         if ({sq[0], sq[i]}) in [['A', 'U'], ['C', 'G']]:
            result = result + cata()

    seqs[sq] =  result
    return result

print cata(seq)