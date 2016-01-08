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

s=sequences[0]
t=sequences[1]
index=0
for i in t:
        a = s[index:].find(i)
        print index+a+1,
        index += a+1
print ""