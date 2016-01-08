from math import factorial

def nPr(n, k):
	'''Returns the number of k-pernumatations of n.'''
	return factorial(n)/factorial(n-k)

rna = "AUAUCUGCGGCAGGACCCAGGGCAAGCUAUUAGCGGGCGCAUUGAUGUGCCUCCACAUAGUAGAGGACACUCGCUAACCACGAAACCGCGACU"

# Counts the number of each times each nucleotide appears in the RNA string.
AU_num = [rna.count(nucleotide) for nucleotide in 'AU']
GC_num = [rna.count(nucleotide) for nucleotide in 'GC']

# There are nPr(max, min) edges for each AU, CG.  Total number of edges is then the product.
max_matchings = nPr(max(AU_num), min(AU_num))*nPr(max(GC_num), min(GC_num))

print max_matchings
with open('D:/python/output.txt', 'w') as output_data:
	output_data.write(str(max_matchings))