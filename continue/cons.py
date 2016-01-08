import sys
desc=[]
seq=[]
for r in sys.stdin.read().split('>'):
    d,s= r.split('\n',1)
    s=''.join(s.split())
    desc.append(d)
    seq.append(s)
print seq[1]