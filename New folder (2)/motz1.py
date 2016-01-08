listt=['AU', 'UA', 'GC', 'CG']
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

descriptions, ss1 = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))
dp=dict()
 
def count(s):
    dp[""] = 1
    if len(s) <= 1:
        return 1
    if s in dp:
        return dp[s]
    t = count(s[1:])
    for k in range(1, len(s)):
        if s[k] + s[0] in listt:
            t += count(s[1:k])*count(s[k+1:])
    t %= 1000000
    dp[s] = t
    return t
print(count(ss1))
del dp
