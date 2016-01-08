import sys
import string

toCompliment = string.maketrans("ACGT", "TGCA")

def give_eq_dist(h, arr, dna1):
  res=[]
  for dna2 in arr:
    if hamming(dna1,dna2) == h \
    or hamming(dna1,complement(dna2)) == h:
      res.append(dna2)
  return res

def complement(sequence):
    return sequence[::-1].translate(toCompliment)

def hamming(reference, comparison):
    hamming_distance = 0
    index = 0
    max_index = len(reference)

    while(index < max_index):
        if(reference[index] != comparison[index]):
            hamming_distance += 1
        index += 1
    return hamming_distance
    
    
arr = sys.stdin.readlines()
arr = [x.strip() for x in arr]

correct = set()
for dna in arr:
  eqlist = give_eq_dist(0, arr, dna)
  if len(eqlist) >= 2:  
    correct.add(dna)

for dna in arr:
  if dna not in correct:
    neigh = give_eq_dist(1, correct, dna) 
    if hamming(dna,neigh[0]) != 1:
      neigh[0] = complement(neigh[0])
    print "%s->%s" % (dna, neigh[0])