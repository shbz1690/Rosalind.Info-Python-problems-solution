from itertools import *
print min((reduce(lambda s,w:(w+s[max(i*(s[:i]==w[-i:])for i in range(99)):],s)[w in s],p)
for p in permutations(input())),key=len)