import itertools
from math import factorial
n = 4
numbers = range(1,n+1)
print(factorial(n)*(2**n))
for p in itertools.permutations(numbers):
     for i in range(2**n):        
          print(' '.join( str(value if i & (1<<j) else -value) for j,value in enumerate(p) ) )
