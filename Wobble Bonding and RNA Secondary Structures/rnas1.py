with open('D:/python/input.txt') as input_data:
	seq = input_data.read().strip()

listt=[['A', 'U'],['U', 'A'],['C', 'G'],['G', 'C'],['U', 'G'],['G', 'U']]
seqs = {}
def rnas(s):
    if s in seqs:
        return seqs[s]
    if len(s) <=4:
        seqs[s]=1
        return 1

    rs = rnas(s[:-1])
    end = s[len(s)-1]
    for i in range(len(s)-4):
        start = s[i]
        if [start, end] in listt:
                rs = rs + rnas(s[0:i])*rnas(s[i+1:-1])
    seqs[s]=rs
    return rs

print rnas(seq)