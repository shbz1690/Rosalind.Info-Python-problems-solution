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
a = [0]*len(dna)
k = 0
for q in range(2, len(dna)):
    while k > 0 and dna[k] != dna[q-1]:
        k = a[k-1]
    if dna[k] == dna[q-1]:
        k += 1
    a[q-1] = k

print ' '.join(map(str, a))