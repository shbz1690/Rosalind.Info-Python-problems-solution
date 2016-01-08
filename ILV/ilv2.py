from scipy.misc import comb


k=5
N =7 
prob = 0
for i in range(N, 2**k + 1):
    prob += comb(2**k, i) * ((1/4.0)**i) * ((3/4.0)**((2**k)-i))

print prob