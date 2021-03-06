def trans():
    transition = transversion = 0
    for p in zip(s1, s2):
        
        if p[0] != p[1]:
            if p in [('G', 'A'), ('A', 'G'), ('C', 'T'), ('T', 'C')]:
                transition += 1
            else:
                transversion += 1
    return float(transition/transversion)

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

descriptions, sequences = parse_fasta(open('D:\python\input.fasta', 'r').read())

s1=sequences[0]
s2=sequences[1]

print trans()