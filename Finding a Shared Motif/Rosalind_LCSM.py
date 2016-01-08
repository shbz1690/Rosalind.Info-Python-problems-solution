# -*- coding: utf-8 -*-
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
new_sequences = sorted(sequences)

def shared_motif(seq):
    substr = ""
    if not seq:
        return substr
    short_seq = min(seq, key=len)
    length = len(short_seq)
    for i in xrange(length):
        for j in xrange(i + len(substr) + 1, length + 1):
            splice = short_seq[i:j]
            if all(splice in l for l in seq):
                substr = splice
    return substr
print shared_motif(new_sequences)