import sys
desc = []
seq=[]
def parse_fasta_file(fasta):
    seq_strings = fasta.strip().split('>')
    for s in seq_strings:
        if len(s):
            sects = s.split()
            k = sects[0]
            v = ''.join(sects[1:])
    desc.append(k)
    seq.append(v)

pal_set=[]
for l in sys.stdin:
    data = open('D:\python\input.txt').read().strip()
parse_fasta_file(data)
data=seq[0]    
for i in range(len(data)):
    for j in range(4,13):
        seq1=data[i:i+j]
        rev=reversed(seq1)
        if i+j<(len(data)+1):
            seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
            rev_comp= ''.join(seq_dict.get(base,base) for base in seq1[::-1])
            if seq1==rev_comp:
                pal_set.append((i+1,j))
print "\n".join([' '.join(map(str, r)) for r in pal_set])