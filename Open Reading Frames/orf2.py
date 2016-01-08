import sys
orf_set = []
index = []
code = { 'TAT': 'Y','CAT': 'H','AAT': 'N','GAT': 'D','TAC': 'Y','CAC': 'H','AAC': 'N','GAC': 'D','TGC': 'C','CGC': 'R','AGC': 'S', 'GGC': 'G',
  'TAA': 'stop_codon', 'CAA': 'Q','AAA': 'K','GAA': 'E','TAG': 'stop_codon','CAG': 'Q','AAG': 'K','GAG': 'E','TGT': 'C','CGT': 'R','AGT': 'S','GGT': 'G',
  'TGA': 'stop_codon','CGA': 'R','AGA': 'R','GGA': 'G','TGG': 'W','CGG': 'R','AGG': 'R','GGG': 'G',
  'TTT': 'F','CTT': 'L','ATT': 'I','GTT': 'V','TTC': 'F','CTC': 'L','ATC': 'I','GTC': 'V','TTA': 'L','CTA': 'L','ATA': 'I','GTA': 'V','TTG': 'L','CTG': 'L','ATG': 'M','GTG': 'V',
  'TCT': 'S','CCT': 'P','ACT': 'T','GCT': 'A','TCC': 'S','CCC': 'P','ACC': 'T','GCC': 'A','TCA': 'S','CCA': 'P','ACA': 'T','GCA': 'A','TCG': 'S','CCG': 'P','ACG': 'T','GCG': 'A'}

def orf_reading(seq):
        for i in range(len(seq)):    
            codon=seq[i:i+3]          
            if code.has_key(codon):
                p_aa1=code[codon]
                if p_aa1 =='M':
                    index.append(i)
        for i in index:
            aa_sequence = ''
            for j in range(i, len(seq),3):
                codon=seq[j:j+3]
                if  code.has_key(codon):
                    p_aa1=code[codon]
                if p_aa1 == 'stop_codon':                    
                    break
                aa_sequence += p_aa1
            if p_aa1=='stop_codon':
                orf_set.append(aa_sequence)
        return orf_set
for line in sys.stdin:
    data = open('D:\python\input.txt').read().strip()   
    a=orf_reading(data)
    rev=reversed(data)
    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
    rev_comp= ''.join(seq_dict.get(base,base) for base in reversed(data))
    b= orf_reading(rev_comp)
    reslst1 = filter(lambda x: x[0] == 'M', a)
    reslst2 = filter(lambda x: x[0] == 'M', b)
    print "\n".join(set(reslst1 + reslst2))
    