from math import factorial

def perm(n, k):
	return factorial(n)/factorial(n-k)

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

descriptions, seqs = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))
rna= seqs[0]

C = rna.count('C')
G = rna.count('G')
A = rna.count('A')
U = rna.count('U')

match = perm(max(A,U), min(A,U))*perm(max(G,C), min(G,C))

print match
