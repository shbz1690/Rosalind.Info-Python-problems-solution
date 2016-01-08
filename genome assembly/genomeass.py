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

descriptions, sequence = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))

def align(seq,acc=''):
    
    if len(seq) == 0:
        return acc
    elif len(acc) == 0:
        acc = seq.pop(0)
        return align(seq, acc)
    else:
        for i in range(len(seq)):
            a = seq[i]
            l = len(a)

            for p in range(l/2):
                q = l - p

                if acc.startswith(a[p:]):
                    seq.pop(i)
                    return align(seq, a[:p] + acc)

                if acc.endswith(a[:q]):
                    seq.pop(i)
                    return align(seq, acc + a[q:])
print align(sequence)
 