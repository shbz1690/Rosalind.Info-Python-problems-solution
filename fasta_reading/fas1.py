desc=[]
seqq=[]
def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))

with open('D:\python\input.txt') as fp:
    for name, seq in read_fasta(fp):
        desc.append(name)
        seqq.append(seq)
print desc