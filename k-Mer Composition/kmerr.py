def parse_fasta (lines):
    descs = []
    seqs = []
    data = ''
    for line in lines:
        if line.startswith('>'):
            if data:
                seqs.append(data)
                data = ''
            descs.append(line)
        else:
            data += line.rstrip('\r\n')
    seqs.append(data)
    return descs, seqs

descriptions, dna1 = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))
dna=dna1[0]

def Kmer_func(k):
    return [ x + y for x in "ACGT" for y in Kmer_func(k-1) ] if k > 0 else [""]

def ab(dna,x):
    return len([ i for i in xrange(len(dna)-len(x)+1) if dna[i:i+len(x)] == x ])

res = Kmer_func(4)
print ' '.join([ str(ab(dna,x)) for x in res ])

