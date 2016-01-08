N=31
k=2
F=[0,1,1]
for i in range (3,N+1):
    s = F[i-1] + k*F[i-2]
    F.append(s)
n=len(F)
print F[n-1]
