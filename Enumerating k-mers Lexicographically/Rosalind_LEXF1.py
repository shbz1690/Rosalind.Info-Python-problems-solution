from itertools import product, chain
n = 4
with open(r'D:\python\input.txt') as data:  
    symbols = chain.from_iterable(x.split() for x in data)
    for prod in (product(symbols,repeat=n)):
        print "".join(prod)