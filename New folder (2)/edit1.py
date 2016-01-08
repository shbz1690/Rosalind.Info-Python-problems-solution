from numpy import zeros

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

# Initialize matrix M.
M = zeros((len(s)+1,len(t)+1), dtype=int)
for i in range(1,len(s)+1):
	M[i][0]= i
for i in range(1,len(t)+1):
	M[0][i]= i

# Compute each entry of M.
for i in xrange(1,len(s)+1):
	for j in xrange(1,len(t)+1):
		if s[i-1] == t[j-1]:
			M[i][j] = M[i-1][j-1]
		else:
			M[i][j] = min(M[i-1][j]+1,M[i][j-1]+1, M[i-1][j-1]+1)

# Print and save the desired edit distance.
print M[len(s)][len(t)]
