n=100
m=18
f=[1,1]*100
for i in range(2,n):
  f[i]=f[i-1]+f[i-2]
  if i>=m:
    f[i]=f[i]-f[(i-m)-1]  
print f[i]