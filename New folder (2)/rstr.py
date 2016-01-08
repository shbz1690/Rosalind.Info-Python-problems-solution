def rstr(dna,gc,n):
    c = [0, 0]
    for codon in dna:
	   if codon in ['C', 'G']:
		  c[0] += 1
	   else:
	       c[1] += 1
    probb = ((0.5*gc)**c[0])*((0.5*(1-gc))**c[1])	  
    p = 1 - (1-probb)**n
    return p
            

with open('D:/python/input.txt') as input_data:
	n, gc, dna = input_data.read().strip().split()
	n = int(n)
	gc = float(gc)
	
print rstr(dna,gc,n)