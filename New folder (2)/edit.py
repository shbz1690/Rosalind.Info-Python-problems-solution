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
s=seqs[0]
t=seqs[1]
n = [range(0,len(s)+1)]

def edit(s,t):
    for k in range(len(t)):
        n.append([k+1] + len(s)*[0])

    for j in range(1,len(s)+1):
        for i in range(1,len(t)+1):
            if s[j-1] == t[i-1]:
                n[i][j] = n[i-1][j-1]
            else:
                n[i][j] = min(n[i-1][j]+1,n[i][j-1]+1,n[i-1][j-1] +1)
    return n[-1][-1]
    
print edit(s,t)