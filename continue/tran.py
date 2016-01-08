def problem(s1, s2):
    transitions = set([('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')])
    ratio = {True: 0.0, False: 0.0}
    for p in zip(s1, s2):
        if p[0] != p[1]:
            ratio[p in transitions] += 1
    return ratio[True] / ratio[False]



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

descriptions, sequences = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))

s1=sequences[0]
s2=sequences[1]

print problem(s1, s2)