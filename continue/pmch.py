from math import factorial

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

descriptions, seq = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))


match = factorial(seq[0].count('A'))*factorial(seq[0].count('C'))
print match

