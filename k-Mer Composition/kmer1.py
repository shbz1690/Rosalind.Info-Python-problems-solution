import itertools
import collections

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

descriptions, s = parse_fasta(open('D:\python\input.fasta', 'r').read().split('\n'))

def kMerComposition(s, k):   
    count = collections.OrderedDict([("".join(a),0) for a in itertools.product("ACGT", repeat=4)])
    for i in range(len(s)-k+1):
        count[s[i:i+4]] += 1
    return count
    

print kMerComposition(s,4)