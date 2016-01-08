from Bio.Seq import Seq
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
dna_seq=sequences[0]
introns=sequences[1:]
posi=[]
leng=[]
for l in introns:
    length=len(l)
    i=dna_seq.find(l)
    dna_seq=dna_seq[0:i]+dna_seq[i+length:]
protein=dna_seq.translate()
print protein


