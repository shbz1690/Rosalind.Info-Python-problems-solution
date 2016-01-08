import sys
Code={'CTC': 'L', 'ATC': 'I', 'GTC': 'V','TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V','TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V','TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V','TTC': 'F',
    'TCT': 'S','CCT': 'P', 'ACT': 'T', 'GCT': 'A','TCC': 'S', 'CCC': 'P','ACC': 'T','GCC': 'A','TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A','TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D','TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D','TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E','TAA': 'Stop', 'CAA': 'Q', 'AAA': 'K','GAA': 'E',
    'TAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E','TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G','TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G','TGA': 'Stop',  'CGA': 'R','AGA': 'R','GGA': 'G',
    'TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G','TGA': 'Stop',  'CGA': 'R', 'AGA': 'R', 'GGA': 'G','TGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G','TGA': 'Stop',  'CGA': 'R','AGA': 'R','GGA': 'G',
    'TGA': 'Stop', 'CGA': 'R','AGA': 'R', 'GGA': 'G','TGG': 'W','CGG': 'R', 'AGG': 'R','GGG': 'G'}
    
def possible_orf(s):
        ORF=[]
        index=[]   
         
        for i in range(len(s)):
            codon=s[i:i+3]
            p_aa1=None
            if len(codon) and Code.has_key(codon):
                p_aa1=Code[codon]
            if p_aa1=='M':
                index.append(i)
        for i in index:
            found_stop=False
            p_aa_seq=''
            for sec_cod in range(i,1,3):
                p_aa1=None
                codon_1=s[sec_cod:sec_cod+3]
                if len(codon_1) and Code.has_key(codon_1):
                    p_aa1=Code[codon_1]
                if not p_aa1:
                    break
                if p_aa1=='Stop':
                    found_stop=True
                    break
                p_aa_seq+=p_aa1
                print p_aa_seq
            if found_stop:
                ORF.append(p_aa_seq)
        return ORF

for line in sys.stdin:
    data = open('D:\python\input.txt').read().strip()
    a=possible_orf(data)
    print a
print

