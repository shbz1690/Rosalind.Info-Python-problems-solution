data = open("D:\python\input.fasta").read().split('>')[1:]
dna = [''.join(x.split('\n')[1:]) for x in data]
print dna[0]
print dna[1]