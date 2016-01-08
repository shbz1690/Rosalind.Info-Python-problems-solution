def RevComp(seq):
        seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
        return "".join([seq_dict[base] for base in reversed(seq.strip())])


with open('D:/python/input.txt') as input_data:
	sets = [line.strip() for line in input_data.readlines()]

edges = set()
for i in sets:
	edges.add(i)
	edges.add(RevComp(i))
	
k = len(sets[0])
edge = lambda elmmt: '('+elmt[0:k-1]+', '+elmt[1:k]+')'
result = [edge(elmt) for elmt in edges]

print '\n'.join(result)
