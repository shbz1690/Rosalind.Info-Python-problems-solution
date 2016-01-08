import sys

def parse_fasta_file(fasta):
    results = []
    seq_strings = fasta.strip().split('>')

    for s in seq_strings:
        if len(s):
            sects = s.split()
            k = sects[0]
            v = ''.join(sects[1:])
            results.append((k, v))

    return results


def overlap_graph(fasta, n):
    results = []

    dna = parse_fasta_file(fasta)

    for k1, v1 in dna:
        for k2, v2 in dna:
            if k1 != k2 and v1.endswith(v2[:n]):
                results.append((k1, k2))

    return results


for line in sys.stdin :    
    data = open('D:/python/input.txt').read()
for edge in overlap_graph(data, 3):
            print edge[0], edge[1]
print
