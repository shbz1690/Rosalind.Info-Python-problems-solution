import sys
records = []
seqq=[]
def fasta_records(my_seq):
    name = my_seq.lstrip('>')
    while name:
        seq = ''
        line = my_seq
        while line and not line.startswith('>'):
            seq += line
            line = my_seq.readline().strip()
        records.append(name)
        seqq.append(seq)
        name = line.lstrip('>')
for line in sys.stdin:
     data = open('D:\python\input.txt').read().strip()
fasta_records(data)
print seqq

            