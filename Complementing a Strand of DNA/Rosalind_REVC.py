import sys
seq=sys.argv[1]
def ReverseComplement1(seq):
        seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
        return "".join([seq_dict[base] for base in reversed(seq.strip())])
for seq1 in sys.stdin:
    a= ReverseComplement1(seq1)
    print a
print
