from itertools import product

n = 4
l = ["A","P","G","T"]

for prod in (product(l,repeat=n)): 
    print("".join(prod))