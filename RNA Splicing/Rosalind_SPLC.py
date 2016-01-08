code = { 'TAT': 'Y','CAT': 'H','AAT': 'N','GAT': 'D','TAC': 'Y','CAC': 'H','AAC': 'N','GAC': 'D','TGC': 'C','CGC': 'R','AGC': 'S', 'GGC': 'G',
  'TAA': 'stop_codon', 'CAA': 'Q','AAA': 'K','GAA': 'E','TAG': 'stop_codon','CAG': 'Q','AAG': 'K','GAG': 'E','TGT': 'C','CGT': 'R','AGT': 'S','GGT': 'G',
  'TGA': 'stop_codon','CGA': 'R','AGA': 'R','GGA': 'G','TGG': 'W','CGG': 'R','AGG': 'R','GGG': 'G',
  'TTT': 'F','CTT': 'L','ATT': 'I','GTT': 'V','TTC': 'F','CTC': 'L','ATC': 'I','GTC': 'V','TTA': 'L','CTA': 'L','ATA': 'I','GTA': 'V','TTG': 'L','CTG': 'L','ATG': 'M','GTG': 'V',
  'TCT': 'S','CCT': 'P','ACT': 'T','GCT': 'A','TCC': 'S','CCC': 'P','ACC': 'T','GCC': 'A','TCA': 'S','CCA': 'P','ACA': 'T','GCA': 'A','TCG': 'S','CCG': 'P','ACG': 'T','GCG': 'A'}
  
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
    
le=len(dna_seq)
protein=''
for i in range(0,le,3):
    aminoacid = code[dna_seq[i:i+3]]
    if aminoacid == 'stop_codon':
        break   
    protein =protein + aminoacid        
print protein