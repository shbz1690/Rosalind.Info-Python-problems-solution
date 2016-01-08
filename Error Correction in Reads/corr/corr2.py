import string

toCompliment = string.maketrans("ACGT", "TGCA")

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

def distt(h, arr, dna1):
  res=[]
  for dna2 in arr:
    if hamming(dna1,dna2) == h \
    or hamming(dna1,complement(dna2)) == h:
      res.append(dna2)
  return res

def complement(sequence):
    return sequence[::-1].translate(toCompliment)

def hamming(reff, compp):
    hamming_distance = 0
    index = 0
    max_index = len(reff)

    while(index < max_index):
        if(reff[index] != compp[index]):
            hamming_distance += 1
        index += 1
    return hamming_distance
    
    
arr = [x.strip() for x in ss1]

correct = set()
for dna in arr:
  eqlist = distt(0, arr, dna)
  if len(eqlist) >= 2:  
    correct.add(dna)

for dna in arr:
  if dna not in correct:
    neigh = distt(1, correct, dna) 
    if hamming(dna,neigh[0]) != 1:
      neigh[0] = complement(neigh[0])
    print "%s->%s" % (dna, neigh[0])