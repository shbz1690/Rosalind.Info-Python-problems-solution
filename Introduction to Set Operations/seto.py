def seto(A):
  print "{" + ", ".join(map(str,A)) + "}"

lines = open('D:/python/input.txt').read().strip().split('\n')
n = int(lines[0])
A = set([int(x) for x in lines[1][1:-1].split(',')])
B = set([int(x) for x in lines[2][1:-1].split(',')])

seto(A|B)
seto(A&B)
seto(A-B)
seto(B-A)
seto([x for x in xrange(1,n+1) if x not in A])
seto([x for x in xrange(1,n+1) if x not in B])